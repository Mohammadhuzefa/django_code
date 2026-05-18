from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Job, Application, EmployeeProfile
from .serializers import JobSerializer, ApplicationSerializer

# --- AUTH VIEWS ---

class RegisterEmployeeView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            if User.objects.filter(username=data.get('username')).exists():
                return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

            # Create User
            user = User.objects.create_user(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password')
            )
            
            # Create Profile
            EmployeeProfile.objects.create(
                user=user,
                phone=data.get('phone'),
                city=data.get('city'),
                profile_pic=request.FILES.get('profile_pic'),
                resume=request.FILES.get('resume')
            )
            return Response({"message": "Registered Successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'is_recruiter': user.is_staff, # is_staff check karna best hai admin ke liye
                'username': user.username
            })
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# --- ADMIN: JOB CRUD ---

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def job_detail(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except Job.DoesNotExist:
        return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        job.delete()
        return Response({"message": "Job deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data)

# --- ADMIN: APPLICATION & EMAIL ---

@api_view(['GET'])
@permission_classes([IsAdminUser])
def all_applications(request):
    apps = Application.objects.all().order_by('-applied_at')
    serializer = ApplicationSerializer(apps, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def update_app_status(request, pk):
    try:
        app = Application.objects.get(pk=pk)
        
        if app.status != 'Pending':
            return Response({"error": "Status already processed!"}, status=400)
            
        new_status = request.data.get('status')
        app.status = new_status
        app.save()

        # --- Email Alert for Acceptance ---
        if new_status == 'Accepted':
            try:
                subject = f"Selection Alert: {app.job.title}"
                message = f"Hi {app.user.username},\n\nYour application for {app.job.title} has been ACCEPTED. Please wait for further contact.\n\nTeam JobPortal"
                send_mail(subject, message, settings.EMAIL_HOST_USER, [app.user.email])
            except:
                pass # Email fail hone pe system na ruke

        return Response({"message": f"Status updated to {app.status}"})
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# --- USER VIEWS ---

@api_view(['GET'])
def get_jobs(request):
    jobs = Job.objects.all().order_by('-posted_at')
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        if Application.objects.filter(user=request.user, job=job).exists():
            return Response({"error": "Already Applied!"}, status=400)
        
        Application.objects.create(user=request.user, job=job)
        return Response({"message": "Applied successfully!"})
    except Job.DoesNotExist:
        return Response({"error": "Job not found"}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_applications(request):
    apps = Application.objects.filter(user=request.user)
    serializer = ApplicationSerializer(apps, many=True)
    return Response(serializer.data)