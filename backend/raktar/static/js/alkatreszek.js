(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        document.body.classList.add('metallic');
        
        // Info modal gomb kezelés (ha van információ gomb a táblázatban)
        const infoButtons = document.querySelectorAll('.btn-info');
        infoButtons.forEach(btn => {
            btn.addEventListener('click', function() {
                const row = this.closest('tr');
                if (row) {
                    const cikkszam = row.querySelector('td:nth-child(1)').textContent.trim();
                    const keszlet = row.querySelector('td:nth-child(2)').textContent.trim();
                    const mertekegyseg = row.querySelector('td:nth-child(3)').textContent.trim();
                    const csoport = row.querySelector('td:nth-child(4)').textContent.trim();
                    const leiras = row.querySelector('td:nth-child(5)').getAttribute('title') || row.querySelector('td:nth-child(5)').textContent.trim();
                    const listaar = row.querySelector('td:nth-child(6)').textContent.trim();
                    
                    // Modal feltöltése
                    document.getElementById('infoCikkszam').textContent = cikkszam;
                    document.getElementById('infoKeszlet').textContent = keszlet + ' ' + mertekegyseg;
                    document.getElementById('infoMertekegyseg').textContent = mertekegyseg;
                    document.getElementById('infoCsoport').textContent = csoport;
                    document.getElementById('infoLeiras').textContent = leiras;
                    document.getElementById('infoListaar').textContent = listaar;
                    
                    // Modal megjelenítése
                    const modal = new bootstrap.Modal(document.getElementById('infoModal'));
                    modal.show();
                }
            });
        });
    });
})();