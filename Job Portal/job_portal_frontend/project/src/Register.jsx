import React, { useState } from 'react';
import axios from 'axios';

function Register() {
  const [formData, setFormData] = useState({ username: '', email: '', password: '', phone: '', city: '' });


  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();
    Object.keys(formData).forEach(key => data.append(key, formData[key]));


    try {
      await axios.post('http://127.0.0.1:8000/api/register/', data);
      alert("Employee Registered!");
    } catch (err) { alert("Registration Failed!"); }
  };

  return (
    <div className="flex min-h-screen font-sans">
      {/* Left Panel */}
      <div className="hidden lg:flex flex-1 bg-gradient-to-br from-indigo-950 via-indigo-800 to-indigo-600 flex-col justify-center px-16 relative overflow-hidden">
        <span className="absolute top-8 left-10 text-xs font-black tracking-[0.2em] text-indigo-400">JW</span>
        <h1 className="text-6xl font-serif font-normal text-white leading-tight mb-6">
          Start your<br /><em>journey.</em>
        </h1>
        <p className="text-indigo-300 text-base leading-relaxed max-w-sm">
          Create your profile and get discovered by top recruiters across the country.
        </p>
        <div className="absolute bottom-12 right-10 grid grid-cols-4 gap-2.5">
          {[...Array(12)].map((_, i) => (
            <span key={i} className="w-1.5 h-1.5 rounded-full bg-indigo-300 opacity-30 block" />
          ))}
        </div>
      </div>

      {/* Right Panel */}
      <div className="flex-1 lg:flex-none lg:w-[540px] flex items-center justify-center bg-slate-50 px-8 py-12">
        <form onSubmit={handleSubmit} className="w-full max-w-md">
          <p className="text-[10px] font-bold tracking-[0.2em] text-indigo-500 mb-2">NEW ACCOUNT</p>
          <h2 className="text-4xl font-serif font-normal text-slate-900 mb-8">Employee Signup</h2>

          <div className="grid grid-cols-2 gap-4 mb-4">
            {[
              { label: 'Username', key: 'username', type: 'text', placeholder: 'your_username' },
              { label: 'Email', key: 'email', type: 'email', placeholder: 'you@email.com' },
              { label: 'Phone', key: 'phone', type: 'text', placeholder: '+91 9876543210' },
              { label: 'City', key: 'city', type: 'text', placeholder: 'Your City' },
            ].map(({ label, key, type, placeholder }) => (
              <div key={key}>
                <label className="block text-[10px] font-bold tracking-widest text-slate-400 uppercase mb-1.5">{label}</label>
                <input
                  type={type}
                  placeholder={placeholder}
                  className="w-full px-3.5 py-2.5 rounded-xl border-2 border-slate-200 bg-white text-slate-900 text-sm outline-none focus:border-indigo-500 transition-colors"
                  onChange={e => setFormData({ ...formData, [key]: e.target.value })}
                />
              </div>
            ))}
          </div>

          <div className="mb-4">
            <label className="block text-[10px] font-bold tracking-widest text-slate-400 uppercase mb-1.5">Password</label>
            <input
              type="password"
              placeholder="••••••••"
              className="w-full px-3.5 py-2.5 rounded-xl border-2 border-slate-200 bg-white text-slate-900 text-sm outline-none focus:border-indigo-500 transition-colors"
              onChange={e => setFormData({ ...formData, password: e.target.value })}
            />
          </div>



          <button
            type="submit"
            className="w-full py-3.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-sm font-bold tracking-wide transition-colors"
          >
            Create Account →
          </button>
        </form>
      </div>
    </div>
  );
}

export default Register;