// Very small demo logic with a tiny in-memory blocklist
const demoBlocklist = ['badguy@example.com', 'phish.com'];

function isBlocked(value){
  if(!value) return false;
  const v = value.trim().toLowerCase();
  if(!v) return false;
  if(v.includes('@')){
    const domain = v.split('@')[1] || '';
    return demoBlocklist.includes(v) || demoBlocklist.includes(domain);
  }
  return demoBlocklist.includes(v);
}

document.addEventListener('DOMContentLoaded', ()=>{
  const btn = document.getElementById('testBtn');
  const input = document.getElementById('senderInput');
  const result = document.getElementById('result');

  function show(message, state){
    result.textContent = message;
    result.className = 'result' + (state ? ' ' + state : '');
  }

  btn.addEventListener('click', ()=>{
    const val = input.value;
    if(!val.trim()){ show('Please enter an email or domain.'); return; }
    if(isBlocked(val)) show(val + ' — BLOCKED', 'blocked');
    else show(val + ' — allowed', 'allowed');
  });

  input.addEventListener('keydown', (e)=>{ if(e.key === 'Enter') btn.click(); });
});
