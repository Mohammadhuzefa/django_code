import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Login({ setIsLoggedIn, setRole }) {
  const [creds, setCreds] = useState({ username: '', password: '' });
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/login/', creds);
      localStorage.setItem('token', res.data.access);
      const userRole = res.data.is_recruiter ? 'recruiter' : 'employee';
      localStorage.setItem('role', userRole);
      setIsLoggedIn(true);
      setRole(userRole);
      if (userRole === 'recruiter') {
        navigate('/admin-dash');
      } else {
        navigate('/user-dash');
      }
    } catch (err) {
      alert("Login Failed: " + (err.response?.data?.error || "Check your credentials"));
    }
  };

  return (
    <div className="flex min-h-screen font-sans">
      {/* Left Panel */}
      <div className="hidden lg:flex flex-1 bg-gradient-to-br from-indigo-950 via-indigo-800 to-indigo-600 flex-col justify-center px-16 relative overflow-hidden">
        <span className="absolute top-8 left-10 text-xs font-black tracking-[0.2em] text-indigo-400">JW</span>
        <h1 className="text-6xl font-serif font-normal text-white leading-tight mb-6">
          Find your<br /><em>next role.</em>
        </h1>
        <p className="text-indigo-300 text-base leading-relaxed max-w-sm">
          Connecting talent with opportunity — one click at a time.
        </p>
        {/* Decorative dots */}
        <div className="absolute bottom-12 right-10 grid grid-cols-4 gap-2.5">
          {[...Array(12)].map((_, i) => (
            <span key={i} className="w-1.5 h-1.5 rounded-full bg-indigo-300 opacity-30 block" />
          ))}
        </div>
      </div>

      {/* Right Panel */}
      <div className="flex-1 lg:flex-none lg:w-[480px] flex items-center justify-center bg-slate-50 px-8">
        <form onSubmit={handleLogin} className="w-full max-w-sm">
          <p className="text-[10px] font-bold tracking-[0.2em] text-indigo-500 mb-2">WELCOME BACK</p>
          <h2 className="text-4xl font-serif font-normal text-slate-900 mb-10">Sign In</h2>

          <div className="mb-5">
            <label className="block text-[11px] font-bold tracking-widest text-slate-400 uppercase mb-1.5">Username</label>
            <input
              type="text"
              placeholder="your_username"
              className="w-full px-4 py-3 rounded-xl border-2 border-slate-200 bg-white text-slate-900 text-sm outline-none focus:border-indigo-500 transition-colors"
              onChange={e => setCreds({ ...creds, username: e.target.value })}
              required
            />
          </div>

          <div className="mb-6">
            <label className="block text-[11px] font-bold tracking-widest text-slate-400 uppercase mb-1.5">Password</label>
            <input
              type="password"
              placeholder="••••••••"
              className="w-full px-4 py-3 rounded-xl border-2 border-slate-200 bg-white text-slate-900 text-sm outline-none focus:border-indigo-500 transition-colors"
              onChange={e => setCreds({ ...creds, password: e.target.value })}
              required
            />
          </div>

          <button
            type="submit"
            className="w-full py-3.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-sm font-bold tracking-wide transition-colors"
          >
            Continue →
          </button>

          <p className="mt-6 text-[10px] text-center text-slate-400 font-bold tracking-widest uppercase">
            Recruiter access: <code className="bg-slate-100 text-indigo-500 px-1.5 py-0.5 rounded font-mono normal-case">admin123</code>
          </p>
        </form>
      </div>
    </div>
  );
}

export default Login;