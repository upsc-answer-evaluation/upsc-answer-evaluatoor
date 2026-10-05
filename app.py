from flask import Flask, Response

app = Flask(__name__)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#ffffff">
<title>UPSC Handwritten Answer Practice</title>
<style>
:root{
  --navy:#172d4f;--ink:#171a20;--muted:#69717c;--line:#d9dee5;--soft:#f6f8fa;
  --green:#157347;--red:#b42318;--warn:#a86100;--shadow:0 2px 12px rgba(0,0,0,.06)
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:#fff;color:var(--ink);font-family:Arial,Helvetica,sans-serif;line-height:1.5}
button{font:inherit;touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.app{width:min(1080px,100%);margin:auto;padding:14px}
header{border-bottom:2px solid var(--navy);padding:5px 1px 13px;margin-bottom:14px}
h1{margin:0;color:var(--navy);font-size:clamp(1.22rem,4.8vw,1.78rem)}
.sub{margin-top:4px;color:var(--muted);font-size:.9rem}
.progress{display:flex;justify-content:space-between;align-items:center;gap:12px;margin:10px 0}
.plabel{font-weight:700;color:var(--navy);font-size:.9rem}
.track{width:150px;max-width:45%;height:6px;background:#e9edf2;border-radius:999px;overflow:hidden}
.fill{height:100%;background:var(--navy);width:33.33%}
.card{border:1px solid var(--line);border-radius:10px;background:#fff;box-shadow:var(--shadow);padding:16px;margin-bottom:13px}
.eyebrow{font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);margin-bottom:6px}
.q{margin:0;font-family:Georgia,"Times New Roman",serif;font-size:clamp(1.05rem,4vw,1.23rem);line-height:1.6;font-weight:600}
.meta{display:flex;flex-wrap:wrap;gap:7px 14px;margin-top:13px;padding-top:10px;border-top:1px solid #e7eaee;color:var(--muted);font-size:.87rem}
.meta strong{color:var(--ink)}
.timerpanel{border:1px solid var(--line);border-radius:10px;background:var(--soft);padding:12px 14px;margin-bottom:13px}
.timerpanel.warning{background:#fff7e6;border-color:#e2b866}
.timerpanel.danger{background:#fff1f0;border-color:#df857d}
.timermain{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.timerbox{display:flex;align-items:baseline;gap:9px}
.tlabel{font-size:.8rem;font-weight:700;color:var(--muted);text-transform:uppercase}
.timer{font:700 clamp(2rem,10vw,3.2rem)/1 "Courier New",monospace;color:var(--navy)}
.warning .timer{color:var(--warn)}.danger .timer{color:var(--red)}
.tstate{margin-top:7px;color:var(--muted);font-size:.88rem;font-weight:700}
.controls{display:flex;flex-wrap:wrap;gap:8px}
.btn{min-height:44px;border:1px solid #adb5c0;border-radius:7px;background:#fff;color:var(--ink);padding:9px 13px;font-weight:700;cursor:pointer}
.btn:disabled{opacity:.4}.primary{background:var(--navy);border-color:var(--navy);color:#fff}
.green{background:var(--green);border-color:var(--green);color:#fff}
.note{border-left:4px solid var(--navy);background:#f8fafc;padding:11px 13px;margin-bottom:13px;font-size:.91rem;color:#39414c}
.workflow{display:grid;grid-template-columns:1fr 1fr;gap:13px}
.step{border:1px solid var(--line);border-radius:10px;padding:15px;background:#fff}
.step h2{margin:0 0 5px;color:var(--navy);font-size:1rem}
.small{font-size:.88rem;color:var(--muted);margin:0 0 10px}
.promptbox{width:100%;min-height:190px;border:1px solid var(--line);border-radius:8px;background:#fafbfc;padding:12px;white-space:pre-wrap;font-size:.86rem;color:#303842;overflow:auto}
.callout{border:1px solid #b9d7c7;background:#f1faf5;border-radius:9px;padding:12px;margin-top:10px;font-size:.89rem}
.nav{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:9px;margin:14px 0}
.nav .prev{justify-self:start}.nav .next{justify-self:end}.navlabel{font-size:.88rem;font-weight:700;color:var(--muted)}
.toast{position:fixed;left:50%;bottom:20px;transform:translate(-50%,20px);background:#20242a;color:#fff;padding:10px 14px;border-radius:7px;opacity:0;pointer-events:none;transition:.18s;max-width:calc(100% - 30px);text-align:center;font-size:.88rem;font-weight:700}
.toast.show{opacity:1;transform:translate(-50%,0)}
@media(max-width:760px){
  .workflow{grid-template-columns:1fr}
  .timermain{align-items:stretch}.timerbox{width:100%;justify-content:space-between}.controls{width:100%}.controls .btn{flex:1 1 30%}
  .nav{grid-template-columns:1fr 1fr}.navlabel{grid-column:1/-1;grid-row:1;text-align:center}.nav .prev{grid-column:1;grid-row:2;width:100%}.nav .next{grid-column:2;grid-row:2;width:100%}
}
</style>
</head>
<body>
<main class="app">
<header>
  <h1>UPSC CSE Mains — Handwritten Answer Practice</h1>
  <div class="sub">GS-II · Separation of Powers · Pen & paper · Evaluate in ChatGPT</div>
</header>

<div class="progress">
  <div class="plabel" id="plabel">Question 1/3</div>
  <div class="track"><div class="fill" id="fill"></div></div>
</div>

<section class="card">
  <div class="eyebrow" id="qno">Question 1</div>
  <p class="q" id="qtext"></p>
  <div class="meta">
    <span><strong>Target:</strong> 150 words</span>
    <span><strong>Time:</strong> 10 minutes</span>
    <span><strong>Marks:</strong> 10</span>
  </div>
</section>

<section class="timerpanel" id="tp">
  <div class="timermain">
    <div class="timerbox">
      <span class="tlabel">Time Left</span>
      <span class="timer" id="timer">10:00</span>
    </div>
    <div class="controls">
      <button class="btn primary" id="start">Start</button>
      <button class="btn" id="pause">Pause</button>
      <button class="btn" id="reset">Reset</button>
    </div>
  </div>
  <div class="tstate" id="tstate">Timer not started.</div>
</section>

<div class="note">
  <strong>Real exam mode:</strong> No typing box. Write your answer physically with pen on paper. After finishing, take clear photos or scan it to PDF.
</div>

<div class="workflow">
  <section class="step">
    <h2>1. Finish your handwritten answer</h2>
    <p class="small">Write within the 10-minute limit. Then photograph/scan all pages clearly and in correct order.</p>
    <button class="btn" id="copyq">Copy Question</button>
  </section>

  <section class="step">
    <h2>2. Open ChatGPT</h2>
    <p class="small">Attach your handwritten answer images/PDF in ChatGPT, then paste the evaluation prompt from this page.</p>
    <div class="controls">
      <button class="btn green" id="openchat">Open ChatGPT</button>
      <button class="btn primary" id="copyprompt">Copy Evaluation Prompt</button>
    </div>
    <div class="callout">
      <strong>No API key or API credits needed here.</strong> You use your normal ChatGPT account directly.
    </div>
  </section>
</div>

<section class="card" style="margin-top:13px">
  <div class="eyebrow">Evaluation Prompt Preview</div>
  <div class="promptbox" id="promptbox"></div>
</section>

<nav class="nav">
  <button class="btn prev" id="prev">← Previous</button>
  <div class="navlabel" id="navlabel">Question 1/3</div>
  <button class="btn next" id="next">Next →</button>
</nav>

<div class="toast" id="toast"></div>
</main>

<script>
const QUESTIONS = [
  {
    id:1,
    text:"The Constitution of India does not envisage a rigid separation of powers, yet it assigns distinct constitutional roles to the principal organs of the State. Examine the nature and significance of this constitutional design."
  },
  {
    id:2,
    text:"Judicial review is indispensable to constitutional government, but judicial intervention may also raise questions of institutional competence and democratic legitimacy. Critically examine in the context of maintaining institutional balance in India."
  },
  {
    id:3,
    text:"Checks and balances in India operate through both constitutional limitations and institutional interaction rather than through watertight separation of powers. Analyse how this arrangement functions in practice while preserving constitutional boundaries."
  }
];

const $ = id => document.getElementById(id);
let idx=0, rem=600, running=false, endTime=null, tick=null, toastTimer=null;

function fmt(s){
  s=Math.max(0,Math.floor(s));
  return String(Math.floor(s/60)).padStart(2,"0")+":"+String(s%60).padStart(2,"0");
}

function sync(){
  if(!running||!endTime)return;
  rem=Math.max(0,Math.ceil((endTime-Date.now())/1000));
  if(rem<=0){
    running=false;
    endTime=null;
    clearInterval(tick);
    tick=null;
  }
}

function renderTimer(){
  $("timer").textContent=fmt(rem);
  $("tp").classList.remove("warning","danger");

  if(rem<=30)$("tp").classList.add("danger");
  else if(rem<=120)$("tp").classList.add("warning");

  if(rem<=0){
    $("tstate").textContent="TIME'S UP";
    $("start").disabled=true;
    $("pause").disabled=true;
    return;
  }

  if(running){
    $("tstate").textContent=rem<=30?"Final 30 seconds.":rem<=120?"2 minutes or less remaining.":"Timer running — write on paper.";
    $("start").textContent="Running";
    $("start").disabled=true;
    $("pause").disabled=false;
  }else{
    $("tstate").textContent=rem<600?"Timer paused.":"Timer not started.";
    $("start").textContent=rem<600?"Resume":"Start";
    $("start").disabled=false;
    $("pause").disabled=true;
  }
}

function resetTimer(){
  running=false; rem=600; endTime=null;
  clearInterval(tick); tick=null;
  renderTimer();
}

function promptFor(q){
return `Evaluate my attached handwritten UPSC CSE Mains answer in strict UPSC examiner mode.

QUESTION:
${q.text}

Paper: GS-II
Topic: Separation of Powers
Target: 150 words
Marks: 10

IMPORTANT:
Evaluate my ORIGINAL handwritten submission first. Do not give me a model answer before evaluating it. Read only what is actually written in my copy; if any handwriting is unclear, explicitly say so rather than inventing content.

Prepare a structured UPSC ASSESSMENT SHEET containing:

1. Exact Question Demand
- Decode the directive word and substantive demand.
- State whether my answer actually addressed that demand.

2. Criterion-wise Assessment and Marks
Give specific feedback and marks for:
- Question demand: /1
- Introduction: /0.5
- Body structure: /1
- Arguments and analytical depth: /2
- Constitutional provisions / Articles: /1
- Supreme Court judgments and examples: /1
- Multiple dimensions, balance and nuance: /1
- Conclusion: /0.5
- Relevance: /1
- Presentation: /1

3. Total Estimated UPSC Marks: /10

4. What I Did Well
Identify only strengths visible in my submitted answer.

5. What Was Missing
Mention specific constitutional, analytical, institutional, case-law, example or dimension gaps that were genuinely relevant to this question.

6. What Should Be Removed / Compressed
Identify repetition, generic statements, irrelevant content, weak examples, unnecessary wording or poor prioritisation.

7. Priority Corrections
Give the 3-5 most important changes that would raise this answer's score.

8. Presentation Assessment
Comment on visible structure, paragraphing, headings/underlining, legibility, spacing and examiner-friendliness where the image permits.

9. Final Examiner Comment
Give a concise overall judgment in the tone of a strict but fair UPSC evaluator.

10. Improved Version
Only AFTER completing the assessment, give a concise improved answer of about 150 words.

Be strict. Do not inflate marks. Do not reward name-dropping unless it is relevant and correctly used.`;
}

function render(){
  const q=QUESTIONS[idx];
  const label=`Question ${idx+1}/${QUESTIONS.length}`;
  $("qno").textContent=`Question ${q.id}`;
  $("qtext").textContent=q.text;
  $("plabel").textContent=label;
  $("navlabel").textContent=label;
  $("fill").style.width=((idx+1)/QUESTIONS.length*100)+"%";
  $("prev").disabled=idx===0;
  $("next").disabled=idx===QUESTIONS.length-1;
  $("promptbox").textContent=promptFor(q);
  resetTimer();
}

function showToast(msg){
  clearTimeout(toastTimer);
  $("toast").textContent=msg;
  $("toast").classList.add("show");
  toastTimer=setTimeout(()=>$("toast").classList.remove("show"),2200);
}

async function copyText(text,msg){
  try{
    await navigator.clipboard.writeText(text);
    showToast(msg);
  }catch(e){
    const ta=document.createElement("textarea");
    ta.value=text; ta.style.position="fixed"; ta.style.opacity="0";
    document.body.appendChild(ta); ta.focus(); ta.select();
    try{document.execCommand("copy");showToast(msg)}catch(err){showToast("Please copy manually.")}
    document.body.removeChild(ta);
  }
}

$("start").onclick=()=>{
  if(running||rem<=0)return;
  running=true;
  endTime=Date.now()+rem*1000;
  renderTimer();
  clearInterval(tick);
  tick=setInterval(()=>{sync();renderTimer()},250);
};

$("pause").onclick=()=>{
  if(!running)return;
  sync(); running=false; endTime=null;
  clearInterval(tick); tick=null;
  renderTimer();
};

$("reset").onclick=resetTimer;
$("copyq").onclick=()=>copyText(`Question ${QUESTIONS[idx].id}: ${QUESTIONS[idx].text}`,"Question copied.");
$("copyprompt").onclick=()=>copyText(promptFor(QUESTIONS[idx]),"Evaluation prompt copied.");
$("openchat").onclick=()=>{
  window.open("https://chatgpt.com/","_blank","noopener");
};

$("prev").onclick=()=>{
  if(idx>0){idx--;render();window.scrollTo({top:0,behavior:"smooth"});}
};
$("next").onclick=()=>{
  if(idx<QUESTIONS.length-1){idx++;render();window.scrollTo({top:0,behavior:"smooth"});}
};

document.addEventListener("visibilitychange",()=>{
  if(!document.hidden){sync();renderTimer();}
});

render();
</script>
</body>
</html>
"""

@app.get("/")
def home():
    return Response(HTML, mimetype="text/html")

@app.get("/health")
def health():
    return {"ok": True}

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "10000")))
