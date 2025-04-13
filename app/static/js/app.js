// filepath: /new_project/new_project/app/static/js/app.js
document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            const username = document.getElementById('username').value.trim();
            const password = document.getElementById('password').value.trim();

            if (!username || !password) {
                event.preventDefault();
                alert('Please fill in both username and password.');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', (event) => {
            const username = document.getElementById('register-username').value.trim();
            const password = document.getElementById('register-password').value.trim();
            const confirmPassword = document.getElementById('confirm-password').value.trim();

            if (!username || !password || !confirmPassword) {
                event.preventDefault();
                alert('Please fill in all fields.');
            } else if (password !== confirmPassword) {
                event.preventDefault();
                alert('Passwords do not match.');
            }
        });
    }
});