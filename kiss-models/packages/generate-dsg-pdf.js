const PDFDocument = require('pdfkit');
const fs = require('fs');

const doc = new PDFDocument({ size: 'LETTER', margin: 50 });
const output = fs.createWriteStream(__dirname + '/dsg-pittsburgh-aug2026.pdf');
doc.pipe(output);

const BRAND_COLOR = '#1a1a2e';
const ACCENT = '#e94560';
const LIGHT_GRAY = '#f5f5f5';

// ---- COVER PAGE ----
doc.rect(0, 0, 612, 792).fill(BRAND_COLOR);

doc.fontSize(14).fillColor('#ffffff').font('Helvetica')
   .text('KiSS MODEL MANAGEMENT', 50, 200, { align: 'center', characterSpacing: 4 });

doc.moveTo(180, 235).lineTo(432, 235).strokeColor(ACCENT).lineWidth(2).stroke();

doc.fontSize(28).fillColor('#ffffff').font('Helvetica-Bold')
   .text("DICK'S SPORTING GOODS", 50, 260, { align: 'center' });

doc.fontSize(16).fillColor(ACCENT).font('Helvetica')
   .text('Pittsburgh — August 2026', 50, 305, { align: 'center' });

doc.fontSize(11).fillColor('#cccccc').font('Helvetica')
   .text('Talent Submission Package', 50, 350, { align: 'center' });

// Contact info at bottom
doc.fontSize(10).fillColor('#888888')
   .text('info@kissmodelmanagement.com  |  202-640-3560', 50, 650, { align: 'center' })
   .text('www.kissmodelmanagement.com  |  @kissmodelsus', 50, 665, { align: 'center' });

// ---- MODEL PAGES ----
const models = [
  { name: 'Alexandra Kiwi', gender: 'F', stats: { Height: '5\'2"', Hair: 'Black', Eyes: 'Brown', Bust: '32"', Cup: 'B', Waist: '30"', Hips: '32"', Shoe: 'US 7', Dress: 'US 2' }},
  { name: 'Bria Reed', gender: 'F', stats: { Height: '5\'8"', Hair: 'Brown', Eyes: 'Hazel', Bust: '32"', Cup: 'B', Waist: '27"', Hips: '33"', Shoe: 'US 7.5', Dress: 'US 4' }},
  { name: 'Izzy Marshall', gender: 'F', stats: { Height: '5\'8"', Hair: 'Blonde', Eyes: 'Blue', Bust: '35"', Waist: '25"', Hips: '36"', Shoe: 'US 7.5' }},
  { name: 'Regina Francen', gender: 'F', stats: { Height: '5\'7"', Hair: 'Brunette', Eyes: 'Brown', Waist: '27"', Hips: '30"' }},
  { name: 'Sandy Evangelista', gender: 'F', stats: { Height: '5\'5"', Hair: 'Brown', Eyes: 'Brown', Bust: '30"', Inseam: '30"', Hips: '32"', Shoe: 'US 8.5', Top: 'XS' }},
  { name: 'Valentina Beli', gender: 'F', stats: { Height: '5\'9"', Hair: 'Dark Blonde', Eyes: 'Blue/Grey', Bust: '32.5"', Waist: '22.5"', Hips: '35.5"' }},
  { name: 'Yulia Fedotova', gender: 'F', stats: { Height: '5\'7"', Hair: 'Brown', Eyes: 'Blue', Bust: '32"', Cup: 'A', Waist: '25"', Hips: '35"', Shoe: 'US 8', Dress: 'US 4-6' }},
  { name: 'Christian Mayer', gender: 'M', stats: { Height: '5\'8"', Hair: 'Blonde', Eyes: 'Blue', Waist: '25"', Hips: '36"', Shoe: 'US 8' }},
  { name: 'Nelson Garcia', gender: 'M', stats: { Height: '5\'8"', Hair: 'Blonde', Eyes: 'Blue', Waist: '25"', Hips: '36"', Shoe: 'US 8' }},
];

for (const model of models) {
  doc.addPage();

  // Header bar
  doc.rect(0, 0, 612, 80).fill(BRAND_COLOR);
  doc.fontSize(10).fillColor('#cccccc').font('Helvetica')
     .text('KiSS MODEL MANAGEMENT', 50, 20, { align: 'left' });
  doc.fontSize(10).fillColor(ACCENT)
     .text("DICK'S SPORTING GOODS — PITTSBURGH AUG 2026", 50, 20, { align: 'right' });

  // Model name
  doc.fontSize(26).fillColor('#ffffff').font('Helvetica-Bold')
     .text(model.name.toUpperCase(), 50, 40, { align: 'left' });

  // Photo placeholder
  const photoX = 50;
  const photoY = 110;
  const photoW = 200;
  const photoH = 280;

  doc.rect(photoX, photoY, photoW, photoH).fill(LIGHT_GRAY);
  doc.rect(photoX, photoY, photoW, photoH).strokeColor('#dddddd').lineWidth(1).stroke();
  doc.fontSize(12).fillColor('#aaaaaa').font('Helvetica')
     .text('Photo', photoX, photoY + photoH / 2 - 10, { width: photoW, align: 'center' });

  // Stats section
  const statsX = 280;
  let statsY = 120;

  doc.fontSize(12).fillColor(ACCENT).font('Helvetica-Bold')
     .text('MEASUREMENTS', statsX, statsY);
  statsY += 25;

  doc.moveTo(statsX, statsY - 5).lineTo(550, statsY - 5).strokeColor(ACCENT).lineWidth(1).stroke();

  const entries = Object.entries(model.stats);
  for (const [key, value] of entries) {
    doc.fontSize(10).fillColor('#666666').font('Helvetica')
       .text(key.toUpperCase(), statsX, statsY, { continued: false });
    doc.fontSize(11).fillColor(BRAND_COLOR).font('Helvetica-Bold')
       .text(value, statsX + 100, statsY);
    statsY += 22;
  }

  // Gender badge
  statsY += 15;
  const genderLabel = model.gender === 'F' ? 'FEMALE' : 'MALE';
  doc.roundedRect(statsX, statsY, 80, 24, 4).fill(ACCENT);
  doc.fontSize(10).fillColor('#ffffff').font('Helvetica-Bold')
     .text(genderLabel, statsX + 5, statsY + 6, { width: 70, align: 'center' });

  // Footer
  doc.fontSize(8).fillColor('#aaaaaa').font('Helvetica')
     .text('info@kissmodelmanagement.com | 202-640-3560 | www.kissmodelmanagement.com | @kissmodelsus', 50, 740, { align: 'center' });
}

doc.end();
output.on('finish', () => {
  console.log('PDF created: kiss-models/packages/dsg-pittsburgh-aug2026.pdf');
  console.log('Size:', fs.statSync(__dirname + '/dsg-pittsburgh-aug2026.pdf').size, 'bytes');
});
