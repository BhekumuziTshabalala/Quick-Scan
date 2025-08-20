import React from 'react';
import styles from './Hero.module.css';

interface HeroProps {
    onOpenAuth: (userType: 'customer' | 'merchant') => void;
}

export default function Hero({ onOpenAuth }: HeroProps) {
    return (
        <section className="hero">
            <div className="container">
                <h1 className="title">
                    Simple Payments for
                    <span className="highlight">Everyone</span>
                </h1>
                <p className="description">
                    Accept payments online or send money securely. Fast, reliable, and built for modern businesses.
                </p>

                <div className="buttons">
                    <button
                        onClick={() => onOpenAuth('customer')}
                        className= "buttons primary">
                        Send Money
                    </button>
                    <button
                        onClick={() => onOpenAuth('merchant')}
                        className="button secondary"
                    >
                        Accept Payments
                    </button>
                </div>
            </div>
        </section>
    );
}