import React from 'react';

interface HeroProps {
  onOpenAuth: (userType: 'customer' | 'merchant') => void;
}

export default function Hero({ onOpenAuth }: HeroProps) {
  return (
    <section className="bg-gray-50 py-20">
      <div className="max-w-4xl mx-auto px-6 text-center">
        <h1 className="text-4xl font-bold text-gray-900 mb-6">
          Simple Payments for
          <span className="block text-blue-600 mt-2">Everyone</span>
        </h1>
        <p className="text-lg text-gray-600 mb-12 max-w-2xl mx-auto">
          Accept payments online or send money securely. Fast, reliable, and built for modern businesses.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4 justify-center max-w-md mx-auto">
          <button
            onClick={() => onOpenAuth('customer')}
            className="bg-blue-600 text-white py-3 px-6 rounded-lg hover:bg-blue-700 transition-colors font-medium"
          >
            Send Money
          </button>
          <button
            onClick={() => onOpenAuth('merchant')}
            className="bg-gray-800 text-white py-3 px-6 rounded-lg hover:bg-gray-900 transition-colors font-medium"
          >
            Accept Payments
          </button>
        </div>
      </div>
    </section>
  );
}