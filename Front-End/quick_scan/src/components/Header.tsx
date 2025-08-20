import React from 'react';
import { CreditCard } from 'lucide-react';
import './Header.css';

export default function Header() {
    return (
        <header className="header">
            <div className="container">
                <div className="brand">
                    <CreditCard className="icon" />
                    <span className="title">PayFlow</span>
                </div>
            </div>
        </header>
    );
}