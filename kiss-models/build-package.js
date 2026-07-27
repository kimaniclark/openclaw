const fs = require('fs');
const path = require('path');

const mainDir = 'model-photos/aali/main';
const mainFiles = fs.readdirSync(mainDir).filter(f => f.endsWith('.jpg') && !f.startsWith('contact') && !f.startsWith('row')).sort();

const profileImg = fs.readFileSync(path.join(mainDir, '040.jpg')).toString('base64');

// Use up to 16 photos for the grid
const gridImages = mainFiles.filter(f => f !== '040.jpg').slice(0, 16).map(f => {
  const data = fs.readFileSync(path.join(mainDir, f)).toString('base64');
  return 'data:image/jpeg;base64,' + data;
});

const gridHtml = gridImages.map(src => `<img src="${src}" />`).join('\n    ');

const html = `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page { size: A4; margin: 0; }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #fff; color: #333; }
  
  .page { width: 210mm; min-height: 297mm; margin: 0 auto; padding: 15mm; }
  
  .header { text-align: center; margin-bottom: 8mm; border-bottom: 2px solid #000; padding-bottom: 5mm; }
  .agency-name { font-size: 11px; letter-spacing: 4px; text-transform: uppercase; color: #666; margin-bottom: 2mm; }
  .model-name { font-size: 36px; font-weight: 300; letter-spacing: 3px; text-transform: uppercase; }
  
  .profile-section { display: flex; gap: 8mm; margin-bottom: 8mm; }
  .profile-image { width: 55%; }
  .profile-image img { width: 100%; height: auto; object-fit: cover; }
  .profile-stats { width: 45%; padding: 5mm 0; }
  
  .stats-table { width: 100%; border-collapse: collapse; }
  .stats-table tr { border-bottom: 1px solid #eee; }
  .stats-table td { padding: 2.5mm 0; font-size: 12px; }
  .stats-table td:first-child { font-weight: 600; text-transform: uppercase; letter-spacing: 1px; font-size: 10px; color: #888; width: 40%; }
  .stats-table td:last-child { font-size: 13px; }
  
  .grid-title { font-size: 10px; letter-spacing: 3px; text-transform: uppercase; color: #888; margin-bottom: 4mm; text-align: center; }
  .photo-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 3mm; }
  .photo-grid img { width: 100%; height: 55mm; object-fit: cover; }
  
  .footer { text-align: center; margin-top: 8mm; padding-top: 4mm; border-top: 1px solid #ddd; }
  .footer p { font-size: 9px; color: #999; letter-spacing: 2px; text-transform: uppercase; }
</style>
</head>
<body>
<div class="page">
  <div class="header">
    <div class="agency-name">Kiss Model Management</div>
    <div class="model-name">Aali</div>
  </div>
  
  <div class="profile-section">
    <div class="profile-image">
      <img src="data:image/jpeg;base64,${profileImg}" />
    </div>
    <div class="profile-stats">
      <table class="stats-table">
        <tr><td>Height</td><td>5&apos;8&quot; / 173 cm</td></tr>
        <tr><td>Bust</td><td>36&quot; / 92 cm</td></tr>
        <tr><td>Cup</td><td>D</td></tr>
        <tr><td>Waist</td><td>29&quot; / 74 cm</td></tr>
        <tr><td>Hips</td><td>41.5&quot; / 106 cm</td></tr>
        <tr><td>Shoe</td><td>US 12 / EU 43</td></tr>
        <tr><td>Hair</td><td>Brown</td></tr>
        <tr><td>Eyes</td><td>Brown</td></tr>
        <tr><td>Ethnicity</td><td>Black / African American</td></tr>
        <tr><td>Location</td><td>Los Angeles, CA</td></tr>
        <tr><td>Age</td><td>30</td></tr>
      </table>
    </div>
  </div>
  
  <div class="grid-title">Portfolio</div>
  <div class="photo-grid">
    ${gridHtml}
  </div>
  
  <div class="footer">
    <p>Kiss Model Management &bull; info@kissmodelmanagement.com &bull; 202-640-3560</p>
    <p>DC &bull; LA &bull; NY</p>
  </div>
</div>
</body>
</html>`;

fs.writeFileSync('model-profiles/aali-package.html', html);
console.log('Package created: ' + mainFiles.length + ' main photos, 16 in grid');
console.log('File size: ' + (fs.statSync('model-profiles/aali-package.html').size / 1024 / 1024).toFixed(1) + ' MB');
