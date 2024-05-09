const toggleBtn = document.querySelector('.toggle-btn')
const toggleBtnIcon = document.querySelector('.toggle-btn i')
const toggleMenu = document.querySelector('.responsive-menu')

toggleBtn.onclick = function () {
    toggleMenu.classList.toggle('open')

    const isOpen = toggleMenu.classList.contains('open')

    toggleBtnIcon.classList = isOpen
        ? 'fa-solid fa-xmark'
        : 'fa-solid fa-bars'
}