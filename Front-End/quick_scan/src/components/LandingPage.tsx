import React, { Component } from 'react';


class LandingPage extends Component {
    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1>Welcome to Quick Scan</h1>
                    <p>Your quick and easy solution for scanning documents.</p>
                </header>
                <main>
                    <section>
                        <h2>Features</h2>
                        <ul>
                            <li>Fast document scanning</li>
                            <li>High-quality image processing</li>
                            <li>User-friendly interface</li>
                        </ul>
                    </section>
                    <section>
                        <h2>Get Started</h2>
                        <p>Click the button below to begin your scanning journey!</p>
                        <button onClick={() => alert('Start Scanning!')}>Start Scanning</button>
                    </section>
                </main>
                <footer className="App-footer">
                    <p>&copy; 2023 Quick Scan. All rights reserved.</p>
                </footer>
            </div>
    );
    }
}

export default LandingPage;
