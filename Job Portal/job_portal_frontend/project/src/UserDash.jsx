import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserDash() {
  const [jobs, setJobs] = useState([]);
  const [appliedJobs, setAppliedJobs] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [activeTab, setActiveTab] = useState("home");
  const [notifications, setNotifications] = useState([
    { id: 1, message: "Your application for Web Developer was viewed.", date: "2 mins ago" },
    { id: 2, message: "New Job Alert: Python Developer in Bhopal", date: "1 hour ago" }
  ]);

  const token = localStorage.getItem('token');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const jobsRes = await axios.get('http://127.0.0.1:8000/api/jobs/');
        setJobs(jobsRes.data);
        if (token) {
          const appliedRes = await axios.get('http://127.0.0.1:8000/api/my-applications/', {
            headers: { Authorization: `Bearer ${token}` }
          });
          setAppliedJobs(appliedRes.data);
        }
      } catch (err) {
        console.error("Data fetch error", err);
      }
    };
    fetchData();
  }, [token]);

  const handleApply = async (jobId) => {
    if (!token) {
      alert("Pehle Login karein!");
      return;
    }
    try {
      await axios.post(`http://127.0.0.1:8000/api/apply/${jobId}/`, {}, {
        headers: { Authorization: `Bearer ${token}` }
      });
      alert("Applied Successfully!");
      const appliedRes = await axios.get('http://127.0.0.1:8000/api/my-applications/', {
        headers: { Authorization: `Bearer ${token}` }
      });
      setAppliedJobs(appliedRes.data);
    } catch (err) {
      alert("Error: " + (err.response?.data?.error || "Already Applied!"));
    }
  };

  const filteredJobs = jobs.filter(job =>
    job.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    job.city.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const navItems = [
    { id: 'home', icon: '⌂', label: 'Browse' },
    { id: 'applied', icon: '✓', label: 'Applied' },
    { id: 'notifications', icon: '◎', label: 'Alerts' },
    { id: 'resume', icon: '◈', label: 'Resume' },
  ];

  // --- SECTIONS ---

  const HomeSection = () => (
    <div>
      <div className="flex flex-col md:flex-row justify-between items-start md:items-end gap-4 mb-8">
        <div>
          <p className="text-[10px] font-bold tracking-[0.2em] text-indigo-500 mb-1">EXPLORE OPPORTUNITIES</p>
          <h1 className="text-4xl font-serif font-normal text-slate-900">Jobs For You</h1>
        </div>
        <div className="relative">
          <span className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 text-sm">🔍</span>
          <input
            type="text"
            placeholder="Search by title or city..."
            className="pl-10 pr-4 py-2.5 rounded-xl border-2 border-slate-200 bg-white text-sm text-slate-800 outline-none focus:border-indigo-500 transition-colors w-64"
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
        {filteredJobs.length > 0 ? filteredJobs.map(job => {
          const isApplied = appliedJobs.some(aj => aj.job === job.id);
          return (
            <div key={job.id} className={`bg-white rounded-2xl p-6 shadow-sm border border-slate-100 flex flex-col gap-3 transition-all ${!isApplied ? 'hover:-translate-y-1 hover:shadow-lg hover:shadow-indigo-50' : ''}`}>
              <div className="flex justify-between items-center">
                <div className="w-11 h-11 rounded-xl bg-indigo-50 flex items-center justify-center text-indigo-600 font-black text-lg">
                  {job.title[0].toUpperCase()}
                </div>
                <span className="text-[10px] font-bold text-slate-400 bg-slate-100 px-2.5 py-1 rounded-full uppercase tracking-wider">
                  {job.city}
                </span>
              </div>
              <div>
                <h3 className="font-bold text-slate-900 uppercase tracking-wide text-sm mb-0.5">{job.title}</h3>
                <p className="text-indigo-600 font-bold text-lg font-serif">₹ {job.salary}</p>
              </div>
              <button
                onClick={() => handleApply(job.id)}
                disabled={isApplied}
                className={`w-full py-2.5 rounded-xl text-xs font-bold tracking-wide transition-colors ${
                  isApplied
                    ? 'bg-slate-100 text-slate-400 cursor-not-allowed'
                    : 'bg-indigo-600 hover:bg-indigo-700 text-white'
                }`}
              >
                {isApplied ? '✓ Applied' : 'Apply Now'}
              </button>
            </div>
          );
        }) : (
          <div className="col-span-full text-center py-20">
            <p className="text-4xl mb-3">🔎</p>
            <p className="text-slate-400 font-semibold text-sm">No jobs found matching your search.</p>
          </div>
        )}
      </div>
    </div>
  );

  const AppliedSection = () => (
    <div className="max-w-2xl">
      <p className="text-[10px] font-bold tracking-[0.2em] text-indigo-500 mb-1">TRACK</p>
      <h2 className="text-4xl font-serif font-normal text-slate-900 mb-8">My Applications</h2>
      <div className="flex flex-col gap-3">
        {appliedJobs.length > 0 ? appliedJobs.map(app => {
          const statusColor = app.status === 'Accepted'
            ? 'border-l-emerald-400'
            : app.status === 'Rejected'
            ? 'border-l-red-400'
            : 'border-l-amber-400';
          const statusText = app.status === 'Accepted'
            ? 'text-emerald-600'
            : app.status === 'Rejected'
            ? 'text-red-500'
            : 'text-amber-600';
          return (
            <div key={app.id} className={`bg-white rounded-2xl px-6 py-4 flex justify-between items-center border-l-4 ${statusColor} shadow-sm`}>
              <div>
                <h4 className="font-bold text-sm text-slate-900 uppercase tracking-wide mb-0.5">{app.job_title}</h4>
                <p className="text-xs text-slate-400">
                  Status: <span className={`font-bold uppercase ${statusText}`}>{app.status || 'Pending'}</span>
                </p>
              </div>
              <p className="text-[11px] text-slate-300 italic">{app.applied_at || 'Recently'}</p>
            </div>
          );
        }) : (
          <div className="bg-white rounded-2xl p-10 text-center">
            <p className="text-slate-400 font-semibold text-sm">You haven't applied to any jobs yet.</p>
          </div>
        )}
      </div>
    </div>
  );

  const NotificationSection = () => (
    <div className="max-w-xl">
      <p className="text-[10px] font-bold tracking-[0.2em] text-indigo-500 mb-1">UPDATES</p>
      <h2 className="text-4xl font-serif font-normal text-slate-900 mb-8">Notifications</h2>
      <div className="flex flex-col gap-3">
        {notifications.map(n => (
          <div key={n.id} className="bg-white rounded-2xl px-6 py-4 flex items-center gap-4 border-l-4 border-l-indigo-500 shadow-sm">
            <span className="w-2 h-2 rounded-full bg-indigo-500 animate-pulse shrink-0" />
            <div>
              <p className="text-sm text-slate-800 font-medium mb-0.5">{n.message}</p>
              <p className="text-xs text-slate-400">{n.date}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  const ResumeSection = () => (
    <div>
      <p className="text-[10px] font-bold tracking-[0.2em] text-indigo-500 mb-1">DOCUMENTS</p>
      <h2 className="text-4xl font-serif font-normal text-slate-900 mb-8">My Resume</h2>
      <div className="bg-white rounded-2xl p-12 max-w-sm border-2 border-dashed border-indigo-100 text-center shadow-sm">
        <p className="text-5xl mb-4">📄</p>
        <p className="text-slate-400 text-sm mb-8 leading-relaxed">Upload your latest CV to attract top recruiters.</p>
        <input type="file" id="cv" className="hidden" />
        <label
          htmlFor="cv"
          className="inline-block px-8 py-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-sm font-bold tracking-wide cursor-pointer transition-colors"
        >
          Upload New PDF
        </label>
      </div>
    </div>
  );

  return (
    <div className="flex min-h-screen bg-slate-50 font-sans">
      {/* Sidebar */}
      <aside className="w-20 bg-indigo-950 flex flex-col items-center pt-6 gap-1 sticky top-0 h-screen shrink-0">
        <span className="text-indigo-400 font-black tracking-widest text-xs mb-5">JW</span>
        {navItems.map(item => (
          <button
            key={item.id}
            onClick={() => setActiveTab(item.id)}
            className={`w-full flex flex-col items-center gap-1 py-3 px-2 rounded-xl transition-all ${
              activeTab === item.id
                ? 'bg-indigo-600/30 text-indigo-300'
                : 'text-indigo-600 hover:text-indigo-400 hover:bg-white/5'
            }`}
          >
            <span className="text-xl leading-none">{item.icon}</span>
            <span className="text-[9px] font-bold tracking-widest uppercase">{item.label}</span>
          </button>
        ))}
      </aside>

      {/* Content */}
      <main className="flex-1 px-10 py-8 overflow-y-auto">
        {activeTab === 'home' && <HomeSection />}
        {activeTab === 'applied' && <AppliedSection />}
        {activeTab === 'notifications' && <NotificationSection />}
        {activeTab === 'resume' && <ResumeSection />}
      </main>
    </div>
  );
}

export default UserDash;