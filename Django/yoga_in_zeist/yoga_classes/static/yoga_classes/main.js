
function showDescription(sessionId) {
    var popup = document.getElementById(sessionId);
    popup.style.display = "block";
}

function closePopup(sessionId) {
    var popup = document.getElementById(sessionId);
    popup.style.display = "none";
}

function showDescription(sessionId) {
    // Закрыть текущее окно
    var currentPopup = document.querySelector('.popup.show');
    if (currentPopup) {
        currentPopup.classList.remove('show');
    }

    // Открыть новое окно
    var newPopup = document.getElementById(sessionId);
    if (newPopup) {
        newPopup.classList.add('show');
    }
}

function closePopup(sessionId) {
    // Закрыть окно
    var popup = document.getElementById(sessionId);
    if (popup) {
        popup.classList.remove('show');
    }
}