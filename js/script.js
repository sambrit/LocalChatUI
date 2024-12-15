document.getElementById('year').textContent = new Date().getFullYear();
function toggleTheme() {
    document.body.dataset.theme = document.body.dataset.theme === 'light' ? 'dark' : 'light';
}
