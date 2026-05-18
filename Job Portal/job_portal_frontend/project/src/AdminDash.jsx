import React, { useEffect, useState } from 'react';
import axios from 'axios';

function AdminDash() {
  const [apps, setApps] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [editingJob, setEditingJob] = useState(null);
  const [newJob, setNewJob] = useState({ title: '', salary: '', city: '', description: '' });

  const token = localStorage.getItem('token');
  const headers = { Authorization: `Bearer ${token}` };

  const fetchData = async () => {
    try {
      const appRes = await axios.get('http://127.0.0.1:8000/api/all-apps/', { headers });
      const jobRes = await axios.get('http://127.0.0.1:8000/api/jobs/');
      setApps(appRes.data);
      setJobs(jobRes.data);
    } catch (err) {
      console.error("Fetch error", err);
    }
  };

  useEffect(() => { fetchData(); }, []);

  const handleStatus = async (id, status) => {
    try {
      await axios.post(`http://127.0.0.1:8000/api/app-status/${id}/`, { status }, { headers });
      alert(`Application ${status}!`);
      fetchData();
    } catch (err) {
      alert("Status update failed");
    }
  };

  const handleAddOrUpdateJob = async (e) => {
    e.preventDefault();
    try {
      if (editingJob) {
        await axios.put(`http://127.0.0.1:8000/api/jobs/${editingJob.id}/`, newJob, { headers });
        alert("Job Updated!");
      } else {
        await axios.post('http://127.0.0.1:8000/api/add-job/', newJob, { headers });
        alert("Job Posted!");
      }
      setNewJob({ title: '', salary: '', city: '', description: '' });
      setEditingJob(null);
      setShowForm(false);
      fetchData();
    } catch (err) {
      alert("Error saving job!");
    }
  };

  const deleteJob = async (id) => {
    if (window.confirm("Are you sure you want to delete this job?")) {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/jobs/${id}/`, { headers });
        fetchData();
      } catch (err) {
        alert("Delete failed!");
      }
    }
  };

  const startEdit = (job) => {
    setEditingJob(job);
    setNewJob({ title: job.title, salary: job.salary, city: job.city, description: job.description });
    setShowForm(true);
    window.scrollTo(0, 0);
  };

  const pendingCount = apps.filter(a => a.status === 'Pending').length;

  return (
    <div className="flex min-h-screen bg-slate-50 font-sans">

      {/* Sidebar */}
      <aside className="w-20 bg-indigo-950 flex flex-col items-center py-6 gap-6 sticky top-0 h-screen shrink-0">
        <span className="text-indigo-400 font-black tracking-widest text-xs">JW</span>
        <span className="text-[9px] text-indigo-600 font-bold tracking-widest uppercase">ADMIN</span>
        <div className="w-8 h-px bg-indigo-800" />
        <div className="flex flex-col items-center gap-0.5">
          <span className="text-2xl font-black text-white leading-none">{jobs.length}</span>
          <span className="text-[9px] text-indigo-500 font-bold tracking-wider uppercase">Jobs</span>
        </div>
        <div className="flex flex-col items-center gap-0.5">
          <span className="text-2xl font-black text-amber-400 leading-none">{pendingCount}</span>
          <span className="text-[9px] text-indigo-500 font-bold tracking-wider uppercase">Pending</span>
        </div>
        <div className="flex flex-col items-center gap-0.5">
          <span className="text-2xl font-black text-white leading-none">{apps.length}</span>
          <span className="text-[9px] text-indigo-500 font-bold tracking-wider uppercase">Total</span>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 px-10 py-8 max-w-5xl">

        {/* Header */}
        <div className="flex justify-between items-end mb-8">
          <div>
            <p className="text-[10px] font-bold tracking-[0.2em] text-indigo-500 mb-1">RECRUITER PANEL</p>
            <h1 className="text-4xl font-serif font-normal text-slate-900">Admin Console</h1>
          </div>
          <button
            onClick={() => { setShowForm(!showForm); setEditingJob(null); setNewJob({ title: '', salary: '', city: '', description: '' }); }}
            className={`px-5 py-2.5 rounded-xl text-sm font-bold tracking-wide transition-colors ${showForm ? 'bg-slate-200 text-slate-600 hover:bg-slate-300' : 'bg-indigo-600 text-white hover:bg-indigo-700'}`}
          >
            {showForm ? '✕ Close' : '+ Post New Job'}
          </button>
        </div>

        {/* Job Form */}
        {showForm && (
          <div className="bg-white rounded-2xl p-7 mb-8 border-2 border-indigo-100 shadow-lg shadow-indigo-50">
            <p className="text-[10px] font-bold tracking-[0.18em] text-indigo-500 mb-5">
              {editingJob ? 'EDITING VACANCY' : 'NEW VACANCY'}
            </p>
            <form onSubmit={handleAddOrUpdateJob}>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                <input
                  type="text" placeholder="Job Title"
                  className="px-4 py-3 rounded-xl border-2 border-slate-200 bg-slate-50 text-sm outline-none focus:border-indigo-500 transition-colors"
                  value={newJob.title}
                  onChange={e => setNewJob({ ...newJob, title: e.target.value })} required
                />
                <input
                  type="text" placeholder="Salary"
                  className="px-4 py-3 rounded-xl border-2 border-slate-200 bg-slate-50 text-sm outline-none focus:border-indigo-500 transition-colors"
                  value={newJob.salary}
                  onChange={e => setNewJob({ ...newJob, salary: e.target.value })} required
                />
                <input
                  type="text" placeholder="City"
                  className="px-4 py-3 rounded-xl border-2 border-slate-200 bg-slate-50 text-sm outline-none focus:border-indigo-500 transition-colors"
                  value={newJob.city}
                  onChange={e => setNewJob({ ...newJob, city: e.target.value })} required
                />
                <textarea
                  placeholder="Job Description"
                  className="md:col-span-3 px-4 py-3 rounded-xl border-2 border-slate-200 bg-slate-50 text-sm outline-none focus:border-indigo-500 transition-colors h-28 resize-none"
                  value={newJob.description}
                  onChange={e => setNewJob({ ...newJob, description: e.target.value })} required
                />
              </div>
              <button
                type="submit"
                className="px-8 py-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-sm font-bold tracking-wide transition-colors"
              >
                {editingJob ? 'Save Changes' : 'Publish Job →'}
              </button>
            </form>
          </div>
        )}

        {/* Active Vacancies */}
        <section className="mb-12">
          <p className="text-[10px] font-bold tracking-[0.2em] text-slate-400 mb-1">MANAGE</p>
          <h2 className="text-2xl font-serif font-normal text-slate-900 mb-5">Active Vacancies</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {jobs.map(job => (
              <div key={job.id} className="bg-white rounded-2xl px-5 py-4 flex justify-between items-center border border-slate-100 shadow-sm hover:shadow-md hover:shadow-indigo-50 transition-shadow">
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 rounded-xl bg-indigo-50 flex items-center justify-center text-indigo-600 font-black text-base shrink-0">
                    {job.title[0].toUpperCase()}
                  </div>
                  <div>
                    <p className="font-bold text-sm text-slate-900 uppercase tracking-wide">{job.title}</p>
                    <p className="text-xs text-slate-400 font-semibold">{job.city} · ₹{job.salary}</p>
                  </div>
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={() => startEdit(job)}
                    className="p-2 rounded-lg bg-slate-100 text-slate-500 hover:bg-indigo-50 hover:text-indigo-600 transition-colors text-sm"
                    title="Edit"
                  >✏</button>
                  <button
                    onClick={() => deleteJob(job.id)}
                    className="p-2 rounded-lg bg-slate-100 text-slate-500 hover:bg-red-50 hover:text-red-500 transition-colors text-sm"
                    title="Delete"
                  >🗑</button>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Applications Inbox */}
        <section>
          <p className="text-[10px] font-bold tracking-[0.2em] text-slate-400 mb-1">INBOX</p>
          <h2 className="text-2xl font-serif font-normal text-slate-900 mb-5 flex items-center gap-3">
            Applications
            {pendingCount > 0 && (
              <span className="text-[10px] font-bold bg-amber-100 text-amber-700 px-2.5 py-1 rounded-full tracking-wide uppercase">
                {pendingCount} pending
              </span>
            )}
          </h2>

          <div className="flex flex-col gap-3">
            {apps.map(app => {
              const isProcessed = app.status === 'Accepted' || app.status === 'Rejected';
              const borderColor = isProcessed
                ? (app.status === 'Accepted' ? 'border-l-emerald-400' : 'border-l-red-400')
                : 'border-l-indigo-500';
              return (
                <div
                  key={app.id}
                  className={`bg-white rounded-2xl px-6 py-4 flex flex-col md:flex-row justify-between items-start md:items-center border-l-4 ${borderColor} shadow-sm ${isProcessed ? 'opacity-60' : ''} transition-all`}
                >
                  <div className="flex items-center gap-4">
                    <div className="w-10 h-10 rounded-full bg-indigo-50 text-indigo-600 font-black text-base flex items-center justify-center shrink-0">
                      {(app.user_name || app.user?.username || '?')[0].toUpperCase()}
                    </div>
                    <div>
                      <p className="font-bold text-sm text-slate-900 uppercase tracking-wide">{app.user_name || app.user?.username}</p>
                      <p className="text-xs text-slate-400">Applied for: {app.job_title || app.job?.title}</p>
                    </div>
                  </div>

                  <div className="mt-3 md:mt-0">
                    {!isProcessed ? (
                      <div className="flex gap-2">
                        <button
                          onClick={() => handleStatus(app.id, 'Accepted')}
                          className="px-5 py-2 bg-emerald-500 hover:bg-emerald-600 text-white rounded-xl text-xs font-bold tracking-wide transition-colors"
                        >Accept</button>
                        <button
                          onClick={() => handleStatus(app.id, 'Rejected')}
                          className="px-5 py-2 bg-red-500 hover:bg-red-600 text-white rounded-xl text-xs font-bold tracking-wide transition-colors"
                        >Reject</button>
                      </div>
                    ) : (
                      <span className={`text-[10px] font-bold px-3 py-1.5 rounded-full uppercase tracking-widest ${app.status === 'Accepted' ? 'bg-emerald-100 text-emerald-700' : 'bg-red-100 text-red-700'}`}>
                        {app.status}
                      </span>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </section>
      </main>
    </div>
  );
}

export default AdminDash;