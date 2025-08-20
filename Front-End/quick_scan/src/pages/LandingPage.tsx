import React, { useState} from 'react';
// @ts-ignore
import Header from "../components/Header.tsx";
// @ts-ignore
import Hero from "../components/Hero.tsx";
// @ts-ignore
import AuthModal from "../components/AuthModal.tsx";


function LandingPage() {
    const [authModal, setAuthModal] = useState<{
        isOpen: boolean;
        userType: 'customer' | 'merchant';
    }>({
        isOpen: false,
        userType: 'customer'
    });

    const openAuthModal = (userType: 'customer' | 'merchant') => {
        setAuthModal({ isOpen: true, userType });
    };

    const closeAuthModal = () => {
        setAuthModal({ isOpen: false, userType: 'customer' });
    };

    return (
        <div className="min-h-screen bg-white">
            <Header />
            <Hero onOpenAuth={openAuthModal} />

            <AuthModal
                isOpen={authModal.isOpen}
                onClose={closeAuthModal}
                userType={authModal.userType}
            />
        </div>
    );
}

export default LandingPage;