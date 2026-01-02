(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        document.body.classList.add('metallic');
        
        const excelBtn = document.querySelector('.btn-excel');
        const pdfBtn = document.querySelector('.btn-pdf');
        
        if (excelBtn) excelBtn.addEventListener('click', exportToExcel);
        if (pdfBtn) pdfBtn.addEventListener('click', exportToPDF);
    });

    function exportToExcel() {
        try {
            const table = document.getElementById('inventoryTable');
            if (!table) {
                alert('Nincs exportálható táblázat!');
                return;
            }

            const rows = Array.from(table.querySelectorAll('tbody tr'));
            if (rows.length === 0) {
                alert('Nincs exportálható adat!');
                return;
            }

            const excelData = rows.map(row => {
                const cells = Array.from(row.querySelectorAll('td'));
                return {
                    'Alkatrész': cells[0]?.textContent.trim() || '',
                    'Alkatrész-csoport': cells[1]?.textContent.trim() || '',
                    'Cikkszám': cells[2]?.textContent.trim() || '',
                    'Mennyiség': cells[3]?.textContent.trim() || '',
                    'Mértékegység': cells[4]?.textContent.trim() || '',
                    'Egységár (Ft)': cells[5]?.textContent.replace(/[^\d]/g, '') || '',
                    'Összár (Ft)': cells[6]?.textContent.replace(/[^\d]/g, '') || ''
                };
            });

            // Összesítő sor
            const totalRow = table.querySelector('tfoot tr');
            if (totalRow) {
                const totalCells = Array.from(totalRow.querySelectorAll('td'));
                excelData.push({
                    'Alkatrész': '',
                    'Alkatrész-csoport': '',
                    'Cikkszám': 'ÖSSZESEN:',
                    'Mennyiség': totalCells[1]?.textContent.trim() || '',
                    'Mértékegység': '',
                    'Egységár (Ft)': '',
                    'Összár (Ft)': totalCells[3]?.textContent.replace(/[^\d]/g, '') || ''
                });
            }

            const ws = XLSX.utils.json_to_sheet(excelData);
            const wb = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(wb, ws, 'Leltár');
            
            const datum = new Date().toISOString().split('T')[0];
            XLSX.writeFile(wb, `leltar_${datum}.xlsx`);
            
        } catch (e) {
            console.error('Excel export hiba:', e);
            alert('Hiba exportálás közben: ' + e.message);
        }
    }

    function exportToPDF() {
        try {
            const table = document.getElementById('inventoryTable');
            if (!table) {
                alert('Nincs exportálható táblázat!');
                return;
            }

            const rows = Array.from(table.querySelectorAll('tbody tr'));
            if (rows.length === 0) {
                alert('Nincs exportálható adat!');
                return;
            }

            const { jsPDF } = window.jspdf;
            const doc = new jsPDF();
            
            doc.setFontSize(18);
            doc.text('Raktár Leltár', 14, 20);
            
            doc.setFontSize(10);
            const datum = new Date().toLocaleDateString('hu-HU');
            doc.text(`Generálva: ${datum}`, 14, 28);
            
            const tableData = rows.map(row => {
                const cells = Array.from(row.querySelectorAll('td'));
                return [
                    cells[0]?.textContent.trim() || '',
                    cells[1]?.textContent.trim() || '',
                    cells[2]?.textContent.trim() || '',
                    cells[3]?.textContent.trim() || '',
                    cells[4]?.textContent.trim() || '',
                    cells[5]?.textContent.trim() || '',
                    cells[6]?.textContent.trim() || ''
                ];
            });
            
            // Összesítő sor
            const totalRow = table.querySelector('tfoot tr');
            if (totalRow) {
                const totalCells = Array.from(totalRow.querySelectorAll('td'));
                tableData.push([
                    '', '', 'ÖSSZESEN:',
                    totalCells[1]?.textContent.trim() || '',
                    '', '',
                    totalCells[3]?.textContent.trim() || ''
                ]);
            }
            
            doc.autoTable({
                startY: 35,
                head: [['Alkatrész', 'Csoport', 'Cikkszám', 'Menny.', 'ME', 'Egységár', 'Összár']],
                body: tableData,
                theme: 'grid',
                styles: {
                    fontSize: 8,
                    cellPadding: 3
                },
                headStyles: {
                    fillColor: [102, 126, 234],
                    textColor: 255,
                    fontStyle: 'bold'
                }
            });
            
            const datumFile = new Date().toISOString().split('T')[0];
            doc.save(`leltar_${datumFile}.pdf`);
            
        } catch (e) {
            console.error('PDF export hiba:', e);
            alert('Hiba exportálás közben: ' + e.message);
        }
    }
})();