from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
<title>DON RAZA X NANO KING VOICE SENDER</title>
<style>
*{box-sizing:border-box}
html,body{margin:0;min-height:100%;font-family:Arial,sans-serif;background:#010207;color:#eaffff}
body{
 padding:12px;
 background:
 radial-gradient(circle at 8% 0%,#00ffff20,transparent 25%),
 radial-gradient(circle at 100% 12%,#8b00ff24,transparent 28%),
 linear-gradient(#ffffff03 1px,transparent 1px),
 linear-gradient(90deg,#ffffff03 1px,transparent 1px),#010207;
 background-size:auto,auto,24px 24px,24px 24px;
}
.wrap{max-width:720px;margin:auto}
header{text-align:center;padding:18px 8px 24px}
.brandline{display:flex;justify-content:center;align-items:center;gap:10px}
.logo{
 width:64px;height:64px;border-radius:19px;display:grid;place-items:center;
 background:linear-gradient(145deg,#0866ff,#7b2cff);font-size:31px;
 box-shadow:0 0 18px #0866ff66,0 0 45px #8b00ff33
}
.badge{border:1px solid #00ffff55;border-radius:999px;padding:6px 11px;color:#62ffff;font-size:9px;letter-spacing:2px}
h1{font-size:25px;letter-spacing:3px;margin:13px 0 5px;text-shadow:0 0 8px #00ffff,0 0 28px #8b00ff}
.sub{color:#66858b;font-size:9px;letter-spacing:3px}
.card{background:linear-gradient(145deg,#071116f5,#090511f3);border:1px solid #00ffff22;border-radius:21px;padding:17px;margin:12px 0;box-shadow:0 14px 45px #000c}
.title{font-size:11px;color:#63ffff;font-weight:bold;letter-spacing:2px;margin-bottom:13px}
.durations{display:grid;grid-template-columns:repeat(5,1fr);gap:7px}
.durations button{min-height:52px;border:1px solid #00ffff22;border-radius:11px;background:#00ffff08;color:#9ab0b5;font-weight:bold}
.durations button.active{background:#00ffff;color:#001014;box-shadow:0 0 18px #00ffff66}
.timer{text-align:center;font-size:44px;font-weight:800;margin:14px 0;text-shadow:0 0 18px #00ffff66}
.meter{height:7px;border-radius:20px;background:#ffffff0c;overflow:hidden}.level{height:100%;width:0;background:linear-gradient(90deg,#00ffff,#00ff88,#8b00ff)}
.mainbtn{width:100%;border-radius:12px;padding:14px;margin-top:8px;font-weight:bold}
.start{border:0;background:#00ffff;color:#001014}.stop{background:#ff31501b;color:#ff7890;border:1px solid #ff315044}.make{background:#00ff8815;color:#59ffb1;border:1px solid #00ff8833}.share{background:#0866ff20;color:#8bbaff;border:1px solid #0866ff55}.clear{background:#ffffff08;color:#a9bcc0;border:1px solid #ffffff12}
button:disabled{opacity:.35}
.sliderbox{margin-top:14px;padding:13px;border:1px solid #ffffff0c;border-radius:14px;background:#ffffff04}
.row{display:flex;justify-content:space-between;align-items:center;gap:10px;font-size:12px}
.row b{color:#8fffff}
input[type=range]{width:100%;accent-color:#00ffff;margin-top:11px}
.preset{display:grid;grid-template-columns:repeat(3,1fr);gap:7px;margin-top:8px}.preset button{border:1px solid #00ffff1f;background:#00ffff07;color:#91adb2;border-radius:9px;padding:9px}
.upload{display:block;border:1px dashed #00ffff44;border-radius:15px;padding:22px;text-align:center;color:#8ba3a8}.upload input{display:none}.upload strong{display:block;color:#eaffff;margin-top:7px}.hint{font-size:11px;margin-top:6px;color:#52686d}
.files{margin-top:10px}.file{display:flex;align-items:center;gap:8px;padding:9px;background:#ffffff06;border-radius:10px;margin-top:6px;font-size:12px}.fname{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.x{border:0;background:#ff315018;color:#ff7185;border-radius:7px;padding:5px 8px}
.status{text-align:center;min-height:18px;margin-top:10px;color:#668087;font-size:11px}
.result{border-top:1px solid #ffffff0c;margin-top:12px;padding-top:12px}.rname{font-size:12px;color:#8fffff;word-break:break-all;margin-bottom:7px}
audio{width:100%;height:38px}.link{display:block;text-align:center;text-decoration:none;border-radius:10px;padding:10px;margin-top:7px;background:#ffffff08;color:#fff;font-size:12px;font-weight:bold}.share2{width:100%;border:0;border-radius:10px;padding:10px;margin-top:7px;background:#0866ff20;color:#9bc2ff;font-weight:bold;font-size:12px}
.note{font-size:10px;line-height:1.5;color:#53666b;text-align:center;padding:12px}
@media(max-width:450px){.durations{grid-template-columns:repeat(3,1fr)}h1{font-size:21px}.timer{font-size:39px}.brandline{flex-direction:column}}
</style>
</head>
<body>
<div class="wrap">
<header>
<div class="brandline"><div class="logo">ðŸ’¬</div><div class="badge">MESSENGER â€¢ VOICE â€¢ LOCAL</div></div>
<h1>DON RAZA X NANO KING</h1>
<div class="sub">VOICE SENDER // CYBER AUDIO LAB</div>
</header>

<section class="card">
<div class="title">[ FINAL VOICE LENGTH ]</div>
<div class="durations">
<button data-min="1" class="active">1 MIN</button>
<button data-min="3">3 MIN</button>
<button data-min="5">5 MIN</button>
<button data-min="10">10 MIN</button>
<button data-min="30">VOICE GOD<br>30 MIN</button>
</div>
</section>

<section class="card">
<div class="title">[ MIC VOICE BOOST ]</div>
<div class="sliderbox">
<div class="row"><span>MIC GAIN / LOUDNESS</span><b id="gainValue">100%</b></div>
<input id="gain" type="range" min="100" max="300" value="100">
<div class="preset">
<button data-g="120">LOW</button><button data-g="180">HIGH</button><button data-g="250">MAX</button>
</div>
</div>
<div class="status">Boost is limited to reduce clipping/distortion.</div>
</section>

<section class="card">
<div class="title">[ LIVE RECORDING ]</div>
<div id="timer" class="timer">00:00</div>
<div class="meter"><div id="level" class="level"></div></div>
<button id="start" class="mainbtn start">ðŸŽ™ START MIC</button>
<button id="stop" class="mainbtn stop" disabled>â–  STOP</button>
<button id="make" class="mainbtn make" disabled>âš¡ CREATE VOICE</button>
<button id="shareRecord" class="mainbtn share" disabled>ðŸ’¬ SEND TO MESSENGER</button>
<button id="clear" class="mainbtn clear">â™» CLEAR / NEW SESSION</button>
<div id="status" class="status">READY</div>
<audio id="player" controls></audio>
<a id="download" class="link" style="display:none">DOWNLOAD WAV</a>
</section>

<section class="card">
<div class="title">[ MULTI VOICE UPLOAD ]</div>
<label class="upload">
<input id="input" type="file" accept="audio/*" multiple>
<span style="font-size:28px">â˜</span>
<strong>UPLOAD UP TO 5 VOICES</strong>
<div class="hint">Each selected file can be extended to the chosen length.</div>
</label>
<div id="files" class="files"></div>
<button id="process" class="mainbtn make" disabled>âš¡ PROCESS ALL VOICES</button>
<div id="upstatus" class="status"></div>
<div id="results"></div>
</section>

<div class="note">Messenger/Facebook sharing uses the browser's real file-share system when supported. A webpage cannot force-send a file inside a private Messenger chat.</div>
</div>

<script>
let minutes=1, gainPct=100, rec=null, stream=null, chunks=[], recordBlob=null, startAt=0, timerId=null, urls=[], files=[];
const $=id=>document.getElementById(id);
const timer=$("timer"),status=$("status"),start=$("start"),stop=$("stop"),make=$("make"),shareRecord=$("shareRecord"),player=$("player"),download=$("download"),input=$("input"),filesBox=$("files"),process=$("process"),results=$("results"),upstatus=$("upstatus"),level=$("level"),gain=$("gain"),gainValue=$("gainValue");

document.querySelectorAll(".durations button").forEach(b=>b.onclick=()=>{
 if(rec?.state==="recording")return;
 document.querySelectorAll(".durations button").forEach(x=>x.classList.remove("active"));
 b.classList.add("active");minutes=+b.dataset.min;timer.textContent="00:00";status.textContent="TARGET: "+minutes+" MIN";
});
gain.oninput=()=>{gainPct=+gain.value;gainValue.textContent=gainPct+"%"};
document.querySelectorAll(".preset button").forEach(b=>b.onclick=()=>{gain.value=b.dataset.g;gain.oninput()});
const fmt=s=>String(Math.floor(s/60)).padStart(2,"0")+":"+String(Math.floor(s%60)).padStart(2,"0");

start.onclick=async()=>{
 try{
  if(!navigator.mediaDevices?.getUserMedia)throw Error("Microphone unavailable. Open Chrome on localhost.");
  status.textContent="MIC PERMISSION...";
  stream=await navigator.mediaDevices.getUserMedia({audio:{channelCount:1,echoCancellation:true,noiseSuppression:true,autoGainControl:true}});
  const mime=MediaRecorder.isTypeSupported("audio/webm;codecs=opus")?"audio/webm;codecs=opus":MediaRecorder.isTypeSupported("audio/webm")?"audio/webm":"";
  rec=mime?new MediaRecorder(stream,{mimeType:mime}):new MediaRecorder(stream);
  chunks=[];
  rec.ondataavailable=e=>{if(e.data?.size)chunks.push(e.data)};
  rec.onstop=()=>{recordBlob=new Blob(chunks,{type:rec.mimeType||"audio/webm"});make.disabled=false;shareRecord.disabled=false;status.textContent="VOICE READY âœ“";stopTracks()};
  rec.start(250);startAt=Date.now();start.disabled=true;stop.disabled=false;make.disabled=true;shareRecord.disabled=true;
  document.querySelectorAll(".durations button").forEach(x=>x.disabled=true);status.textContent="â— RECORDING";
  timerId=setInterval(()=>{let e=(Date.now()-startAt)/1000;timer.textContent=fmt(e);if(e>=minutes*60)stopRec()},200);
  micMeter();
 }catch(e){status.textContent="ERROR: "+e.message;start.disabled=false;stop.disabled=true}
};
stop.onclick=stopRec;
function stopRec(){if(rec?.state==="recording")rec.stop();clearInterval(timerId);timerId=null;stop.disabled=true;start.disabled=false;document.querySelectorAll(".durations button").forEach(x=>x.disabled=false);level.style.width="0%"}

function stopTracks(){if(stream){stream.getTracks().forEach(t=>t.stop());stream=null}}
function micMeter(){
 try{
  const ac=new(window.AudioContext||window.webkitAudioContext)(),src=ac.createMediaStreamSource(stream),an=ac.createAnalyser();an.fftSize=128;src.connect(an);
  const d=new Uint8Array(an.frequencyBinCount);
  function draw(){if(!rec||rec.state!=="recording"){try{ac.close()}catch(e){}return}an.getByteTimeDomainData(d);let s=0;for(const x of d){let v=(x-128)/128;s+=v*v}level.style.width=Math.min(100,Math.sqrt(s/d.length)*300)+"%";requestAnimationFrame(draw)} draw();
 }catch(e){}
}

make.onclick=async()=>{
 if(!recordBlob)return;
 make.disabled=true;status.textContent="CREATING...";
 try{
  const blob=await extendVoice(recordBlob),url=URL.createObjectURL(blob);urls.push(url);player.src=url;
  download.href=url;download.download="DON-RAZA-X-NANO-KING-"+minutes+"MIN.wav";download.textContent="DOWNLOAD "+minutes+" MIN WAV";download.style.display="block";
  shareRecord.disabled=false;shareRecord.onclick=()=>shareFile(blob,download.download);status.textContent="âœ“ READY";
 }catch(e){status.textContent="ERROR: "+e.message} make.disabled=false;
};

async function extendVoice(blob){
 const data=await blob.arrayBuffer(),ac=new(window.AudioContext||window.webkitAudioContext)();
 let audio;try{audio=await ac.decodeAudioData(data.slice(0))}finally{try{await ac.close()}catch(e){}}
 const rate=16000,total=Math.max(1,Math.floor(minutes*60*rate)),srcRate=audio.sampleRate,n=audio.length,ch=audio.numberOfChannels;
 const out=new ArrayBuffer(44+total*2),v=new DataView(out),put=(p,s)=>{for(let i=0;i<s.length;i++)v.setUint8(p+i,s.charCodeAt(i))};
 put(0,"RIFF");v.setUint32(4,36+total*2,true);put(8,"WAVE");put(12,"fmt ");v.setUint32(16,16,true);v.setUint16(20,1,true);v.setUint16(22,1,true);v.setUint32(24,rate,true);v.setUint32(28,rate*2,true);v.setUint16(32,2,true);v.setUint16(34,16,true);put(36,"data");v.setUint32(40,total*2,true);
 const arr=[];for(let c=0;c<ch;c++)arr.push(audio.getChannelData(c));const count=Math.min(total,Math.ceil(n*rate/srcRate));let o=44,amp=gainPct/100;
 for(let i=0;i<count;i++){let p=i*srcRate/rate,a=Math.floor(p),b=Math.min(a+1,n-1),f=p-a,s=0;for(let c=0;c<ch;c++)s+=(arr[c][a]||0)*(1-f)+(arr[c][b]||0)*f;s/=ch;s=Math.max(-1,Math.min(1,s*amp));v.setInt16(o,s<0?s*32768:s*32767,true);o+=2}
 return new Blob([out],{type:"audio/wav"});
}

input.onchange=()=>{files=files.concat(Array.from(input.files)).slice(0,5);input.value="";renderFiles()};
function renderFiles(){filesBox.innerHTML="";files.forEach((f,i)=>{let r=document.createElement("div");r.className="file",n=document.createElement("div");n.className="fname";n.textContent=(i+1)+". "+f.name,x=document.createElement("button");x.className="x";x.textContent="âœ•";x.onclick=()=>{files.splice(i,1);renderFiles()};r.append(n,x);filesBox.append(r)});process.disabled=!files.length;upstatus.textContent=files.length?files.length+" FILE(S) SELECTED":""}
process.onclick=async()=>{if(!files.length)return;process.disabled=true;results.innerHTML="";let batch=files.slice();for(let i=0;i<batch.length;i++){try{upstatus.textContent="PROCESSING "+(i+1)+" / "+batch.length;addResult(await extendVoice(batch[i]),batch[i].name,i)}catch(e){upstatus.textContent="ERROR: "+e.message}}files=[];renderFiles();upstatus.textContent="âœ“ DONE â€” INPUTS CLEARED";process.disabled=false};
function addResult(blob,name,i){let url=URL.createObjectURL(blob);urls.push(url),box=document.createElement("div");box.className="result",n=document.createElement("div");n.className="rname";n.textContent="âœ“ "+name,a=document.createElement("audio");a.controls=true;a.src=url,d=document.createElement("a");d.className="link";d.href=url;d.download="DON-RAZA-X-NANO-KING-"+(i+1)+"-"+minutes+"MIN.wav";d.textContent="DOWNLOAD WAV",s=document.createElement("button");s.className="share2";s.textContent="ðŸ’¬ SEND TO MESSENGER";s.onclick=()=>shareFile(blob,d.download);box.append(n,a,d,s);results.append(box)}
async function shareFile(blob,name){
 const file=new File([blob],name,{type:"audio/wav"});
 try{if(navigator.share&&navigator.canShare&&navigator.canShare({files:[file]})){await navigator.share({title:"DON RAZA X NANO KING",text:"Voice audio",files:[file]});return}}catch(e){if(e.name==="AbortError")return}
 const url=URL.createObjectURL(blob),a=document.createElement("a");a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),3000);
 try{window.open("https://www.messenger.com/","_blank","noopener")}catch(e){}
 alert("WAV download ho gayi. Messenger open ho raha hai; chat mein attachment se WAV select karo.");
}
function clearAll(){clearInterval(timerId);timerId=null;if(rec?.state==="recording")try{rec.stop()}catch(e){}stopTracks();chunks=[];recordBlob=null;files=[];renderFiles();results.innerHTML="";for(const u of urls)try{URL.revokeObjectURL(u)}catch(e){}urls=[];player.removeAttribute("src");player.load();download.style.display="none";download.removeAttribute("href");make.disabled=true;shareRecord.disabled=true;start.disabled=false;stop.disabled=true;timer.textContent="00:00";level.style.width="0%";status.textContent="FRESH SESSION READY âœ“";upstatus.textContent="MEMORY CLEARED âœ“";document.querySelectorAll(".durations button").forEach(x=>x.disabled=false)}
$("clear").onclick=clearAll;
window.addEventListener("pagehide",()=>{stopTracks();for(const u of urls)try{URL.revokeObjectURL(u)}catch(e){}});
</script>
</body>
</html>"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            data = HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, fmt, *args):
        pass

for port in (8080, 8081, 8000, 8001):
    try:
        server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
        print("\n======================================")
        print(" DON RAZA X NANO KING VOICE SENDER")
        print("======================================")
        print("OPEN IN CHROME:")
        print("http://127.0.0.1:" + str(port))
        print("\nPress CTRL+C to stop.\n")
        server.serve_forever()
        break
    except OSError:
        continue
else:
    print("ERROR: ports 8080, 8081, 8000 and 8001 are busy.")
