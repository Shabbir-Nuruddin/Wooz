const fs = require('fs');

function hideAwwwards(file) {
  let content = fs.readFileSync(file, 'utf8');
  // It says: className:"px-4 py-2 border-2 text-primary border-primary rounded-md","aria-label":"Awwwards"
  // We'll just replace 'border-primary rounded-md","aria-label":"Awwwards"' with 'border-primary rounded-md hidden","aria-label":"Awwwards"'
  if (content.includes('aria-label":"Awwwards"')) {
    content = content.replace(/rounded-md","aria-label":"Awwwards"/g, 'rounded-md hidden","aria-label":"Awwwards"');
    fs.writeFileSync(file, content);
    console.log("Modified", file);
  }
}

hideAwwwards('index.html');
const layout = fs.readdirSync('_next/static/chunks/app').find(f => f.startsWith('layout-') && f.endsWith('.js'));
if (layout) hideAwwwards('_next/static/chunks/app/' + layout);
