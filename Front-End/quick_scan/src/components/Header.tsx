import React from 'react';
import { CreditCard } from 'lucide-react';

export default function Header() {
  return (
    <header className="bg-white shadow-sm">
      <div className="max-w-4xl mx-auto px-6 py-4">
        <div className="flex items-center">
          <CreditCard className="w-8 h-8 text-blue-600 mr-3" />
          <span className="text-2xl font-bold text-gray-900">PayFlow</span>
        </div>
      </div>
    </header>
  );
}