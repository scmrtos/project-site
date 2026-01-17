document.addEventListener('DOMContentLoaded', function() {
    // Ищем все ячейки таблиц в основном контенте
    const cells = document.querySelectorAll('.rst-content table.docutils td');
    cells.forEach(cell => {
        let html = cell.innerHTML;
        // Заменяем голые символы на версию с span
        html = html.replace(/✔/g, '<span class="symbol-check">✔</span>');
        html = html.replace(/✘/g, '<span class="symbol-cross">✘</span>');
        cell.innerHTML = html;
    });
});