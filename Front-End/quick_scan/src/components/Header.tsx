import React from 'react';
import { QrCode } from 'lucide-react';
import './Header.css';

export default function Header() {
    return (
        <header className="header">
            <div className="container">
                <div className="brand">
                    <QrCode className="icon" />
                    <span className="title">Quick-Scan</span>
                </div>
            </div>
        </header>
    );
}