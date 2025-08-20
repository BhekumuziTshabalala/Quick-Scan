import React, { useState } from 'react';
import { X, Mail, Lock } from 'lucide-react';

import './AuthModal.css';

interface AuthModalProps {
    isOpen: boolean;
    onClose: () => void;
    userType: 'customer' | 'merchant';
}

export default function AuthModal({ isOpen, onClose, userType }: AuthModalProps) {
    const [isLogin, setIsLogin] = useState(true);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    if (!isOpen) return null;

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        console.log('Form submitted:', { userType, isLogin, email, password });
    };
    return (
        <div className="overlay">
            <div className="modal">
                <div className="header">
                    <h2 className="title">
                        {isLogin ? 'Sign In' : 'Sign Up'} - {userType === 'customer' ? 'Personal Account' : 'Business Account'}
                    </h2>
                    <button onClick={onClose} className="closeButton">
                        <X className="closeIcon" />
                    </button>
                </div>

                <div className="content">
                    <form onSubmit={handleSubmit} className="form">
                        <div className="field">
                            <label className="label">Email</label>
                            <div className="inputWrapper">
                                <Mail className="inputIcon" />
                                <input
                                    type="email"
                                    value={email}
                                    onChange={(e) => setEmail(e.target.value)}
                                    className="input"
                                    placeholder="your@email.com"
                                    required
                                />
                            </div>
                        </div>

                        <div className="field">
                            <label className="label">Password</label>
                            <div className="inputWrapper">
                                <Lock className="inputIcon" />
                                <input
                                    type="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                    className="input"
                                    placeholder="••••••••"
                                    required
                                />
                            </div>
                        </div>

                        <button type="submit" className="submitButton">
                            {isLogin ? 'Sign In' : 'Sign Up'}
                        </button>
                    </form>

                    <div className="toggle">
                        <button
                            onClick={() => setIsLogin(!isLogin)}
                            className="toggleButton"
                        >
                            {isLogin ? "Don't have an account? Sign up" : "Already have an account? Sign in"}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}