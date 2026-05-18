import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import UserDash from './UserDash';
import AdminDash from './AdminDash';
import './App.css'

const Home = () => (
  <div className="min-h-screen flex flex-col font-sans">

    {/* Hero Section */}
    <section className="flex-1 flex flex-col items-center justify-center text-center bg-gradient-to-br from-indigo-950 via-indigo-800 to-indigo-600 px-6 py-36 relative overflow-hidden">
      {/* Background decorative circles */}
      <div className="absolute top-[-80px] left-[-80px] w-[400px] h-[400px] bg-indigo-500 opacity-10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-[-60px] right-[-60px] w-[350px] h-[350px] bg-indigo-300 opacity-10 rounded-full blur-3xl pointer-events-none" />

      <p className="text-[10px] font-bold tracking-[0.3em] text-indigo-300 uppercase mb-4">
        Trusted by 10,000+ Students in Bhopal
      </p>
      <h1 className="text-5xl md:text-7xl font-serif font-normal text-white leading-tight max-w-3xl mb-6">
        Find your<br /><em>dream job.</em>
      </h1>
      <p className="text-indigo-300 text-base md:text-lg max-w-md mb-12 leading-relaxed">
        Your next career move starts here. Browse hundreds of opportunities across Madhya Pradesh.
      </p>
      <div className="flex flex-col sm:flex-row gap-4">
        <Link
          to="/register"
          className="px-10 py-4 bg-white text-indigo-700 rounded-xl font-bold text-sm tracking-wide hover:bg-indigo-50 transition-colors shadow-xl"
        >
          Get Started →
        </Link>
        <Link
          to="/login"
          className="px-10 py-4 border-2 border-indigo-400 text-indigo-200 rounded-xl font-bold text-sm tracking-wide hover:bg-indigo-800 transition-colors"
        >
          Sign In
        </Link>
      </div>

      {/* Stats row */}
      <div className="mt-20 flex flex-wrap justify-center gap-12">
        {[
          { num: '10,000+', label: 'Students Placed' },
          { num: '500+', label: 'Active Jobs' },
          { num: '200+', label: 'Companies' },
        ].map(({ num, label }) => (
          <div key={label} className="text-center">
            <p className="text-3xl font-serif font-normal text-white">{num}</p>
            <p className="text-[11px] font-bold tracking-widest text-indigo-400 uppercase mt-1">{label}</p>
          </div>
        ))}
      </div>
    </section>

    {/* Feature Cards */}
    <section className="bg-slate-50 py-24 px-6">
      <div className="max-w-5xl mx-auto">
        <p className="text-[10px] font-bold tracking-[0.25em] text-indigo-500 text-center mb-3">WHY JOBS</p>
        <h2 className="text-3xl md:text-4xl font-serif font-normal text-slate-900 text-center mb-14">
          Everything you need to land a role
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {[
            { icon: '🎯', title: 'Curated Listings', desc: 'Jobs handpicked for freshers and experienced professionals in MP.' },
            { icon: '⚡', title: 'One-Click Apply', desc: 'Apply instantly without lengthy forms or redundant steps.' },
            { icon: '📊', title: 'Track Applications', desc: 'Know exactly where your application stands — in real time.' },
          ].map(({ icon, title, desc }) => (
            <div key={title} className="bg-white rounded-2xl p-8 border border-slate-100 shadow-sm hover:shadow-md hover:shadow-indigo-50 transition-shadow">
              <span className="text-3xl mb-4 block">{icon}</span>
              <h3 className="font-bold text-slate-900 text-sm uppercase tracking-wide mb-2">{title}</h3>
              <p className="text-slate-400 text-sm leading-relaxed">{desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>

    {/* CTA Banner */}
    <section className="bg-indigo-600 py-20 px-6 text-center">
      <h2 className="text-3xl md:text-4xl font-serif font-normal text-white mb-4">Ready to get started?</h2>
      <p className="text-indigo-200 text-sm mb-8">Join thousands of job seekers already using JobWay.</p>
      <Link
        to="/register"
        className="inline-block px-10 py-4 bg-white text-indigo-700 rounded-xl font-bold text-sm tracking-wide hover:bg-indigo-50 transition-colors shadow-lg"
      >
        Create Free Account →
      </Link>
    </section>
  </div>
);

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [role, setRole] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    const savedRole = localStorage.getItem('role');
    if (token && savedRole) {
      setIsLoggedIn(true);
      setRole(savedRole);
    }
  }, []);

  const handleLogout = () => {
    localStorage.clear();
    setIsLoggedIn(false);
    setRole(null);
  };

  return (
    <Router>
      <div className="min-h-screen flex flex-col font-sans bg-slate-50">

        {/* NAVBAR */}
        <header className="bg-white/80 backdrop-blur-md border-b border-slate-100 sticky top-0 z-50">
          <nav className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">

            {/* Brand */}
            <Link to="/" className="text-indigo-600 font-black tracking-[0.15em] text-lg uppercase">
              JOBS
            </Link>

            {/* Center Links */}
            <div className="hidden md:flex items-center gap-8 text-[11px] font-bold text-slate-500 uppercase tracking-widest">
              <Link to="/" className="hover:text-indigo-600 transition-colors">Home</Link>
              {isLoggedIn && role === 'employee' && (
                <Link to="/user-dash" className="hover:text-indigo-600 transition-colors">Dashboard</Link>
              )}
              {isLoggedIn && role === 'recruiter' && (
                <Link to="/admin-dash" className="text-indigo-600 font-black hover:text-indigo-700 transition-colors">
                  ★ Admin Panel
                </Link>
              )}
            </div>

            {/* Auth Buttons */}
            <div className="flex items-center gap-3">
              {!isLoggedIn ? (
                <>
                  <Link
                    to="/login"
                    className="text-[11px] font-bold text-slate-500 hover:text-indigo-600 transition-colors uppercase tracking-widest px-3 py-2"
                  >
                    Login
                  </Link>
                  <Link
                    to="/register"
                    className="px-5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-[11px] font-bold tracking-widest uppercase transition-colors"
                  >
                    Sign Up
                  </Link>
                </>
              ) : (
                <button
                  onClick={handleLogout}
                  className="px-5 py-2 bg-red-50 hover:bg-red-100 text-red-500 rounded-xl text-[11px] font-bold tracking-widest uppercase transition-colors active:scale-95"
                >
                  Logout
                </button>
              )}
            </div>
          </nav>
        </header>

        {/* BODY */}
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/register" element={<Register />} />
            <Route path="/login" element={<Login setIsLoggedIn={setIsLoggedIn} setRole={setRole} />} />
            <Route path="/user-dash" element={role === 'employee' ? <UserDash /> : <Navigate to="/login" />} />
            <Route path="/admin-dash" element={role === 'recruiter' ? <AdminDash /> : <Navigate to="/login" />} />
          </Routes>
        </main>

        {/* FOOTER */}
        <footer className="bg-indigo-950 text-slate-500 py-14 px-6">
          <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6 border-t border-indigo-900 pt-10">
            <div>
              <p className="text-white font-black tracking-[0.2em] uppercase text-sm mb-1">Jobs Portal</p>
              <p className="text-[11px] uppercase tracking-widest text-indigo-600">Bhopal Hub, Madhya Pradesh</p>
            </div>
            <div className="flex gap-8 text-[11px] font-bold uppercase tracking-widest">
              <Link to="/" className="hover:text-indigo-400 transition-colors">Home</Link>
              <Link to="/login" className="hover:text-indigo-400 transition-colors">Login</Link>
              <Link to="/register" className="hover:text-indigo-400 transition-colors">Register</Link>
            </div>
            <p className="text-[11px] uppercase tracking-widest text-indigo-800">© 2026 All Rights Reserved</p>
          </div>
        </footer>

      </div>
    </Router>
  );
}

export default App;