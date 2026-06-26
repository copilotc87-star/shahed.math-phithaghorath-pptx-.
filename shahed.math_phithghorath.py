import webbrowser
import os

# ==========================================
# بخش ۱: تابع ساخت اسلاید
# ==========================================
def make_slide(n, title, body):
    return f"""
    <div class="slide" id="s{n}">
        <div class="page-num">اسلاید {n} از ۵۵</div>
        <h1>{title}</h1>
        {body}
        <div class="nav">
            <button onclick="go(1)">🏠</button>
            <button onclick="go({n-1})">◀</button>
            <button onclick="go({n+1})">▶</button>
            <button class="blue" onclick="go(11)">🧮</button>
            <button class="green" onclick="go(16)">🎮</button>
        </div>
    </div>"""

# ==========================================
# بخش ۲: HTML اصلی
# ==========================================
html = """<!DOCTYPE html>
<html lang="fa">
<head>
<meta charset="UTF-8">
<title>فیثاغورث - ۵۵ اسلاید</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Arial;background:#1a1a2e;color:#fff}
.slide{display:none;max-width:900px;margin:20px auto;background:#16213e;padding:30px;border-radius:16px;min-height:500px}
.slide.active{display:block}
h1{color:#f1c40f;text-align:center;font-size:2.2em;margin:15px 0}
h2{color:#3498db;text-align:center;margin:10px 0}
.page-num{text-align:center;color:#666;font-size:.85em;margin-bottom:10px}
.nav{display:flex;gap:8px;justify-content:center;margin-top:30px;flex-wrap:wrap;border-top:1px solid #333;padding-top:15px}
.nav button{padding:8px 16px;border:none;border-radius:20px;background:#333;color:#fff;cursor:pointer;font-size:.9em}
.nav button:hover{opacity:.8}
.nav .blue{background:#2980b9}
.nav .green{background:#27ae60}
.box{background:#0f3460;padding:20px;border-radius:12px;margin:15px 0;line-height:2}
.formula{text-align:center;font-size:2.5em;color:#f1c40f;padding:20px;background:#0f3460;border-radius:12px;margin:15px 0}
.row{display:flex;gap:15px;flex-wrap:wrap;margin:15px 0}
.col{flex:1;min-width:200px;background:#0f3460;padding:20px;border-radius:12px;text-align:center}
.col-title{color:#3498db;font-size:1.2em;margin-bottom:10px}
.display{font-size:2em;padding:15px;background:#1a1a2e;border-radius:8px;margin:10px 0}
.display.red{color:#e74c3c;border:2px solid #e74c3c}
.display.blue{color:#3498db;border:2px solid #3498db}
.btn-row{display:flex;gap:6px;flex-wrap:wrap;justify-content:center;margin:8px 0}
.btn{padding:8px 14px;border:none;border-radius:8px;background:#555;color:#fff;cursor:pointer;font-size:.9em}
.btn:hover{opacity:.8}
.btn.blue{background:#2980b9}
.btn.red{background:#e74c3c}
.btn.green{background:#27ae60}
.btn.active-blue{background:#3498db;box-shadow:0 0 10px #3498db}
.btn.active-red{background:#e74c3c;box-shadow:0 0 10px #e74c3c}
.result{background:#0f3460;padding:20px;border-radius:12px;margin:15px 0;text-align:center}
.result-main{font-size:1.8em;color:#2ecc71}
.result-detail{color:#aaa;margin-top:8px;line-height:1.8}
.quiz-btn{display:block;width:100%;padding:15px;margin:10px 0;background:#0f3460;border:2px solid #333;border-radius:10px;color:#fff;font-size:1.1em;cursor:pointer;text-align:right}
.quiz-btn:hover{border-color:#3498db}
.quiz-btn.correct{background:#27ae60;border-color:#2ecc71}
.quiz-btn.wrong{background:#e74c3c;border-color:#c0392b}
.fact{background:#0f3460;padding:12px;margin:8px 0;border-right:3px solid #f1c40f;border-radius:4px}
input[type=number]{width:100%;padding:12px;font-size:1.1em;border-radius:8px;border:1px solid #555;background:#1a1a2e;color:#fff;text-align:center;margin:8px 0}
</style>
</head>
<body>

<div id="app"></div>

<script>
// ==========================================
// داده‌های ۵۵ اسلاید
// ==========================================
const slides = [];

function addSlide(title, type, data){
    slides.push({title, type, data});
}

// اسلاید ۱-۵: مقدمه
addSlide("🎓 قضیه فیثاغورث", "title", "ارائه جامع مهندسی | ۵۵ اسلاید | ماشین حساب کامل");
addSlide("📋 فهرست", "list", ["۱-۵: مقدمه و تاریخچه","۶-۱۰: اثبات‌ها","۱۱-۲۰: ماشین حساب مهندسی","۲۱-۳۰: ثلاثی‌های فیثاغورثی","۳۱-۴۵: کاربردها","۴۶-۵۵: آزمون و جمع‌بندی"]);
addSlide("👤 فیثاغورث که بود؟", "text", "فیثاغورث (۵۷۰-۴۹۵ ق.م) فیلسوف و ریاضیدان یونان باستان. بنیانگذار مکتب فیثاغورثی در کروتون ایتالیا. جمله معروف: «همه چیز عدد است». شاگردانش معتقد بودند اعداد اساس جهان هستند.");
addSlide("🏛 مکتب فیثاغورثی", "text", "ترکیبی از ریاضیات، فلسفه و عرفان. اعتقاد به تناسخ ارواح. گیاه‌خواری. کشف نسبت‌های هارمونیک در موسیقی. تأثیر عمیق بر افلاطون و ارسطو.");
addSlide("📐 مثلث قائم‌الزاویه", "text", "مثلثی با یک زاویه ۹۰ درجه. ضلع مقابل زاویه قائمه: وَتَر (بزرگترین ضلع). دو ضلع دیگر: ساق‌ها (قاعده و ارتفاع). مجموع زوایای داخلی: ۱۸۰ درجه.");

// اسلاید ۶-۱۰: اثبات‌ها
addSlide("📝 بیان قضیه", "formula", "a² + b² = c²");
addSlide("🖼 اثبات تصویری", "text", "مربعی به ضلع (a+b) رسم کنید. ۴ مثلث قائم‌الزاویه یکسان داخل آن قرار دهید. مساحت ناحیه خالی میانی = c². این برابر است با a² + b².");
addSlide("📐 اثبات اقلیدسی", "text", "اقلیدس در کتاب «اصول» (۳۰۰ ق.م): با رسم ارتفاع از رأس قائمه، مثلث به دو مثلث متشابه تقسیم می‌شود. از تناسب اضلاع، قضیه اثبات می‌شود.");
addSlide("🔢 اثبات جبری", "text", "(a+b)² = a² + 2ab + b²\\nمساحت ۴ مثلث = 2ab\\nمساحت مربع داخلی = c²\\n∴ a² + 2ab + b² = c² + 2ab\\n∴ a² + b² = c²");
addSlide("🎨 اثبات داوینچی", "text", "لئوناردو داوینچی با استفاده از تقارن و برش اشکال هندسی، اثباتی هنری و بصری برای قضیه فیثاغورث ارائه داد که نشان می‌دهد مساحت‌ها برابرند.");

// اسلاید ۱۱-۱۵: ماشین حساب مهندسی
addSlide("🧮 محاسبه وتر", "calc1", "");
addSlide("🧮 محاسبه ضلع مجهول", "calc2", "");
addSlide("🧮 بررسی مثلث", "calc3", "");
addSlide("🧮 محاسبه مساحت", "calc4", "");
addSlide("🧮 محاسبه محیط", "calc5", "");

// اسلاید ۱۶: ماشین حساب زنده
addSlide("🎮 ماشین حساب زنده", "live", "");

// اسلاید ۱۷-۲۰: مثال‌ها
addSlide("📐 مثال ۳-۴-۵", "example", [3,4]);
addSlide("📐 مثال ۵-۱۲-۱۳", "example", [5,12]);
addSlide("📐 مثال ۸-۱۵-۱۷", "example", [8,15]);
addSlide("📐 مثال ۷-۲۴-۲۵", "example", [7,24]);

// اسلاید ۲۱-۳۰: ثلاثی‌ها
addSlide("⭐ ثلاثی‌های فیثاغورثی", "triples", "");
addSlide("📊 فرمول اقلیدس", "generator", "");
addSlide("📊 جدول تا ۵۰", "table", 50);
addSlide("📊 جدول ۵۰-۱۰۰", "table", 100);
addSlide("🔍 ثلاثی‌های اولیه", "text", "ثلاثی اولیه: بزرگترین مقسوم‌علیه مشترک a,b,c برابر ۱ باشد. مثال: (3,4,5) اولیه است، (6,8,10) اولیه نیست.");
addSlide("📜 لوح Plimpton 322", "text", "لوح گلی بابلی (۱۸۰۰ ق.م) شامل ۱۵ ثلاثی فیثاغورثی. این نشان می‌دهد بابلی‌ها ۱۰۰۰ سال قبل از فیثاغورث این رابطه را می‌شناختند.");
addSlide("🏛 مصر باستان", "text", "مصریان از مثلث ۳-۴-۵ برای ساخت اهرام استفاده می‌کردند. طناب‌های ۱۲ گره‌ای برای ایجاد زاویه قائمه.");
addSlide("🇨🇳 چین باستان", "text", "در چین باستان «قضیه گوگو» نام داشت. کتاب «چوپی سوانجینگ» (۵۰۰ ق.م) شامل این قضیه است.");
addSlide("🇮🇳 هند باستان", "text", "در «شولبا سوترا» (۸۰۰ ق.م) هند، این قضیه برای ساخت محراب‌های ودایی استفاده می‌شد.");
addSlide("🇮🇷 فیثاغورث در ایران", "text", "برخی منابع از سفر فیثاغورث به ایران و آشنایی با ریاضیات زرتشتی خبر می‌دهند. خیام نیز به این قضیه اشاره کرده است.");

// اسلاید ۳۱-۴۵: کاربردها
const apps = [
    ["🏗","معماری","محاسبه ارتفاع ساختمان، طراحی سقف، روش ۳-۴-۵ در ساخت و ساز"],
    ["🧭","GPS و ناوبری","کوتاه‌ترین فاصله بین دو نقطه روی کره زمین"],
    ["🤖","رباتیک","محاسبه مسیر حرکت بازوی ربات در فضای ۲D و ۳D"],
    ["🎮","بازی‌سازی","فاصله بین کاراکترها، تشخیص برخورد"],
    ["🏥","پزشکی","تصویربرداری MRI و CT Scan، بازسازی سه‌بعدی"],
    ["🚀","فضانوردی","مسیر فضاپیماها، فاصله ستارگان"],
    ["📡","مخابرات","ارتفاع و فاصله آنتن‌ها، قدرت سیگنال"],
    ["🎵","موسیقی","نسبت‌های هارمونیک، فاصله نت‌ها"],
    ["🔬","نانوتکنولوژی","فواصل اتمی، طراحی مولکولی"],
    ["🎨","هنر و طراحی","پرسپکتیو، تناسبات طلایی"],
    ["⚽","ورزش","محاسبه مسافت در زمین‌های ورزشی"],
    ["🌊","اقیانوس‌شناسی","عمق‌یابی با سونار"],
    ["✈","هوانوردی","مسیر پرواز، ارتفاع"],
    ["🏔","نقشه‌برداری","مثلث‌بندی، ارتفاع کوه‌ها"],
    ["💻","گرافیک کامپیوتری","رندرینگ سه‌بعدی، واقعیت مجازی"]
];
apps.forEach(([icon,title,desc]) => addSlide(`${icon} ${title}`, "app", {icon, title, desc}));

// اسلاید ۴۶-۵۵: پیشرفته و جمع‌بندی
addSlide("🔢 اعداد گنگ", "text", "کشف √۲ (قطر مربع به ضلع ۱) بحرانی در مکتب فیثاغورثی ایجاد کرد. آنها معتقد بودند همه چیز عدد (گویا) است! هیپاسوس این راز را فاش کرد و اعدام شد.");
addSlide("🌌 فضای n بعدی", "text", "d² = Σ(xᵢ-yᵢ)²\\nتعمیم قضیه فیثاغورث به فضاهای با ابعاد بالاتر. اساس یادگیری ماشین و هوش مصنوعی.");
addSlide("💡 حقایق جالب ۱", "facts", ["۳۷۰+ اثبات مختلف","۲۵۰۰+ سال قدمت","شناخته شده در ۵ تمدن","اینشتین در ۱۱ سالگی اثبات نوشت","گارفیلد (رئیس جمهور) اثبات دارد"]);
addSlide("💡 حقایق جالب ۲", "facts", ["فیثاغورث ۱۰۰ گاو قربانی کرد","در چین «قضیه گوگو»","اساس مثلثات و هندسه","بدون آن GPS نبود","۲۰+ رشته علمی کاربرد"]);
addSlide("🎯 آزمون ۱", "quiz", {q:"کدام ثلاثی فیثاغورثی است؟",opts:["3-4-5","2-3-4","1-2-3","4-5-6"],ans:0});
addSlide("🎯 آزمون ۲", "quiz", {q:"فرمول اصلی کدام است؟",opts:["a²+b²=c²","a+b=c","a²-b²=c²","ab=c²"],ans:0});
addSlide("🎯 آزمون ۳", "quiz", {q:"فیثاغورث اهل کجا بود؟",opts:["یونان","مصر","چین","هند"],ans:0});
addSlide("🎯 آزمون ۴", "quiz", {q:"بزرگترین ضلع مثلث قائم‌الزاویه؟",opts:["وتر","قاعده","ارتفاع","ساق"],ans:0});
addSlide("📊 آمار", "text", "• ۳۷۰+ اثبات مختلف\\n• ۲۵۰۰+ سال قدمت\\n• ۲۰+ رشته علمی\\n• ۵ تمدن باستانی\\n• ۱۰۰+ ثلاثی فیثاغورثی");
addSlide("💬 نقل قول‌ها", "text", "«همه چیز عدد است» - فیثاغورث\\n«ریاضیات زبان طبیعت است» - گالیله\\n«هندسه دانش اندازه‌گیری جهان است» - افلاطون");
addSlide("🔮 آینده", "text", "کامپیوترهای کوانتومی، هوش مصنوعی، یادگیری ماشین، واقعیت مجازی - همگی از قضیه فیثاغورث در محاسبات استفاده می‌کنند.");
addSlide("📚 منابع", "text", "۱. اصول اقلیدس\\n۲. تاریخ ریاضیات - بویر\\n۳. قضیه فیثاغورث - الی مائور\\n۴. Wikipedia - Pythagorean Theorem");
addSlide("🎓 جمع‌بندی", "text", "قضیه فیثاغورث:\\n• بنیادی‌ترین قضیه هندسه\\n• پل بین جبر و هندسه\\n• اساس مثلثات\\n• کاربرد در تمام علوم\\n• a² + b² = c²");
addSlide("❤️ سپاس", "text", "با تشکر از توجه شما!\\n\\nاین ارائه تعاملی با Python و JavaScript ساخته شد.\\n\\nریاضیات را دوست داشته باشید.");
addSlide("🏁 پایان", "text", "🎉\\n\\nامیدوارم لذت برده باشید!\\n\\nبرای بازگشت به خانه روی دکمه 🏠 کلیک کنید.\\n\\nهمواره در حال یادگیری باشید ❤️");

// ==========================================
// متغیرها
// ==========================================
let cur = 1;
let la = 3, lb = 4;

// ==========================================
// رندر اسلاید
// ==========================================
function render(n){
    let s = slides[n-1];
    let h = `<div class="page-num">اسلاید ${n} از ۵۵</div><h1>${s.title}</h1>`;
    
    if(s.type==="title"){
        h += `<h2>${s.data}</h2><div class="formula">a² + b² = c²</div>`;
    }else if(s.type==="list"){
        s.data.forEach(l => h += `<div class="box">${l}</div>`);
    }else if(s.type==="text"){
        h += `<div class="box">${s.data.replace(/\\n/g,'<br>')}</div>`;
    }else if(s.type==="formula"){
        h += `<div class="formula">${s.data}</div>`;
    }else if(s.type==="calc1"){
        h += `<div class="box">
            <input type="number" id="c1a" placeholder="ضلع a" value="3">
            <input type="number" id="c1b" placeholder="ضلع b" value="4">
            <button class="btn green" onclick="calc1()" style="width:100%;margin-top:10px;padding:12px">محاسبه وتر (c)</button>
            <div class="result" id="c1r" style="display:none"></div></div>`;
    }else if(s.type==="calc2"){
        h += `<div class="box">
            <input type="number" id="c2a" placeholder="ضلع معلوم" value="3">
            <input type="number" id="c2c" placeholder="وتر (c)" value="5">
            <button class="btn green" onclick="calc2()" style="width:100%;margin-top:10px;padding:12px">محاسبه ضلع مجهول</button>
            <div class="result" id="c2r" style="display:none"></div></div>`;
    }else if(s.type==="calc3"){
        h += `<div class="box">
            <input type="number" id="c3a" placeholder="ضلع a" value="3">
            <input type="number" id="c3b" placeholder="ضلع b" value="4">
            <input type="number" id="c3c" placeholder="ضلع c" value="5">
            <button class="btn green" onclick="calc3()" style="width:100%;margin-top:10px;padding:12px">بررسی قائم‌الزاویه بودن</button>
            <div class="result" id="c3r" style="display:none"></div></div>`;
    }else if(s.type==="calc4"){
        h += `<div class="box">
            <input type="number" id="c4a" placeholder="قاعده" value="3">
            <input type="number" id="c4b" placeholder="ارتفاع" value="4">
            <button class="btn green" onclick="calc4()" style="width:100%;margin-top:10px;padding:12px">محاسبه مساحت</button>
            <div class="result" id="c4r" style="display:none"></div></div>`;
    }else if(s.type==="calc5"){
        h += `<div class="box">
            <input type="number" id="c5a" placeholder="ضلع a" value="3">
            <input type="number" id="c5b" placeholder="ضلع b" value="4">
            <button class="btn green" onclick="calc5()" style="width:100%;margin-top:10px;padding:12px">محاسبه محیط</button>
            <div class="result" id="c5r" style="display:none"></div></div>`;
    }else if(s.type==="live"){
        h += `<div class="row">
        <div class="col"><div class="col-title">🔵 مقدار a</div>
        <div class="display blue" id="liveA">a = 3</div>
        <div class="btn-row">
            <button class="btn active-blue" onclick="setA(3,this)">3</button>
            <button class="btn" onclick="setA(5,this)">5</button>
            <button class="btn" onclick="setA(8,this)">8</button>
            <button class="btn" onclick="setA(12,this)">12</button>
        </div>
        <div class="btn-row">
            <button class="btn red" onclick="chA(-1)">-1</button>
            <button class="btn green" onclick="chA(1)">+1</button>
        </div></div>
        <div class="col"><div class="col-title">🔴 مقدار b</div>
        <div class="display red" id="liveB">b = 4</div>
        <div class="btn-row">
            <button class="btn active-red" onclick="setB(4,this)">4</button>
            <button class="btn" onclick="setB(12,this)">12</button>
            <button class="btn" onclick="setB(15,this)">15</button>
            <button class="btn" onclick="setB(24,this)">24</button>
        </div>
        <div class="btn-row">
            <button class="btn red" onclick="chB(-1)">-1</button>
            <button class="btn green" onclick="chB(1)">+1</button>
        </div></div></div>
        <div class="result"><div class="result-main" id="liveForm">3² + 4² = 5²</div>
        <div class="result-detail" id="liveDet">c = √(9+16) = 5.00</div></div>`;
    }else if(s.type==="example"){
        let [a,b] = s.data;
        let c = Math.sqrt(a*a+b*b);
        h += `<div class="formula">${a}² + ${b}² = ${c.toFixed(0)}²</div>
        <div class="box">${a}² = ${a*a} | ${b}² = ${b*b} | ${a*a}+${b*b}=${a*a+b*b} | c=√${a*a+b*b}=${c.toFixed(2)}</div>`;
    }else if(s.type==="triples"){
        [[3,4,5],[5,12,13],[8,15,17],[7,24,25],[9,40,41],[11,60,61],[12,35,37],[13,84,85],[20,21,29],[28,45,53]].forEach(t => {
            h += `<div class="box">${t[0]}-${t[1]}-${t[2]} | ${t[0]}²+${t[1]}²=${t[0]*t[0]}+${t[1]*t[1]}=${t[2]*t[2]}=${t[2]}² ✓</div>`;
        });
    }else if(s.type==="generator"){
        h += `<div class="box">
            <input type="number" id="gm" placeholder="m (m>n)" value="3">
            <input type="number" id="gn" placeholder="n" value="1">
            <button class="btn green" onclick="gen()" style="width:100%;margin-top:10px;padding:12px">تولید ثلاثی</button>
            <div class="result" id="gr" style="display:none"></div>
            <p style="margin-top:10px;color:#aaa">فرمول: a=m²-n², b=2mn, c=m²+n²</p></div>`;
    }else if(s.type==="table"){
        let max = s.data;
        h += `<div class="box">`;
        for(let m=2;m<=12;m++){
            for(let n=1;n<m;n++){
                let a=m*m-n*n, b=2*m*n, c=m*m+n*n;
                if(c<=max && c>(max-50)) h += `(${a},${b},${c}) `;
            }
        }
        h += `</div>`;
    }else if(s.type==="app"){
        h += `<div class="box" style="text-align:center">
            <div style="font-size:4em">${s.data.icon}</div>
            <h2>${s.data.title}</h2>
            <p style="font-size:1.2em">${s.data.desc}</p></div>`;
    }else if(s.type==="facts"){
        s.data.forEach(f => h += `<div class="fact">🔸 ${f}</div>`);
    }else if(s.type==="quiz"){
        h += `<p style="text-align:center;font-size:1.3em;margin:20px">${s.data.q}</p>`;
        s.data.opts.forEach((opt,i) => {
            h += `<button class="quiz-btn" onclick="checkQuiz(${i},${s.data.ans},this,${n})">${String.fromCharCode(65+i)}) ${opt}</button>`;
        });
        h += `<p id="qf${n}" style="text-align:center;margin-top:15px;font-size:1.2em"></p>`;
    }
    
    // ناوبری
    h += `<div class="nav">
        <button onclick="go(1)">🏠 خانه</button>
        <button onclick="go(${n-1})" ${n===1?'disabled':''}>◀ قبلی</button>
        <button onclick="go(${n+1})" ${n===55?'disabled':''}>بعدی ▶</button>
        <button class="blue" onclick="go(11)">🧮 ماشین حساب</button>
        <button class="green" onclick="go(16)">🎮 زنده</button>
        <button onclick="go(21)">⭐ ثلاثی‌ها</button>
        <button onclick="go(46)">🎯 آزمون</button>
    </div>`;
    
    document.getElementById('app').innerHTML = h;
    window.scrollTo(0,0);
}

function go(n){
    if(n<1 || n>55) return;
    cur = n;
    render(n);
}

// توابع محاسباتی
function calc1(){
    let a=parseFloat(document.getElementById('c1a').value)||0;
    let b=parseFloat(document.getElementById('c1b').value)||0;
    let c=Math.sqrt(a*a+b*b);
    document.getElementById('c1r').style.display='block';
    document.getElementById('c1r').innerHTML=`<div class="result-main">c = ${c.toFixed(4)}</div><div class="result-detail">√(${a}² + ${b}²) = √(${a*a} + ${b*b}) = √${a*a+b*b}</div>`;
}
function calc2(){
    let a=parseFloat(document.getElementById('c2a').value)||0;
    let c=parseFloat(document.getElementById('c2c').value)||0;
    document.getElementById('c2r').style.display='block';
    if(c<=a){document.getElementById('c2r').innerHTML='⚠ وتر باید بزرگتر از ضلع باشد';return;}
    let b=Math.sqrt(c*c-a*a);
    document.getElementById('c2r').innerHTML=`<div class="result-main">b = ${b.toFixed(4)}</div><div class="result-detail">√(${c}² - ${a}²) = √(${c*c} - ${a*a}) = √${c*c-a*a}</div>`;
}
function calc3(){
    let a=parseFloat(document.getElementById('c3a').value)||0;
    let b=parseFloat(document.getElementById('c3b').value)||0;
    let c=parseFloat(document.getElementById('c3c').value)||0;
    let sides=[a,b,c].sort((x,y)=>x-y);
    let ok=Math.abs(sides[0]*sides[0]+sides[1]*sides[1]-sides[2]*sides[2])<0.001;
    document.getElementById('c3r').style.display='block';
    document.getElementById('c3r').innerHTML=ok?'<div class="result-main" style="color:#2ecc71">✅ بله! مثلث قائم‌الزاویه است</div>':'<div class="result-main" style="color:#e74c3c">❌ خیر. قائم‌الزاویه نیست</div>';
}
function calc4(){
    let a=parseFloat(document.getElementById('c4a').value)||0;
    let b=parseFloat(document.getElementById('c4b').value)||0;
    document.getElementById('c4r').style.display='block';
    document.getElementById('c4r').innerHTML=`<div class="result-main">مساحت = ${(a*b/2).toFixed(4)}</div><div class="result-detail">½ × ${a} × ${b}</div>`;
}
function calc5(){
    let a=parseFloat(document.getElementById('c5a').value)||0;
    let b=parseFloat(document.getElementById('c5b').value)||0;
    let c=Math.sqrt(a*a+b*b);
    document.getElementById('c5r').style.display='block';
    document.getElementById('c5r').innerHTML=`<div class="result-main">محیط = ${(a+b+c).toFixed(4)}</div><div class="result-detail">${a} + ${b} + ${c.toFixed(4)}</div>`;
}
function gen(){
    let m=parseInt(document.getElementById('gm').value)||2;
    let n=parseInt(document.getElementById('gn').value)||1;
    document.getElementById('gr').style.display='block';
    if(m<=n){document.getElementById('gr').innerHTML='⚠ m باید بزرگتر از n باشد';return;}
    let a=m*m-n*n, b=2*m*n, c=m*m+n*n;
    document.getElementById('gr').innerHTML=`<div class="result-main">(${a}, ${b}, ${c})</div><div class="result-detail">${a}² + ${b}² = ${a*a} + ${b*b} = ${c*c} = ${c}² ✓</div>`;
}

function setA(v,btn){
    la=v;
    document.querySelectorAll('#app .col:first-child .btn').forEach(b=>{b.classList.remove('active-blue');});
    btn.classList.add('active-blue');
    updateLive();
}
function setB(v,btn){
    lb=v;
    document.querySelectorAll('#app .col:last-child .btn').forEach(b=>{b.classList.remove('active-red');});
    btn.classList.add('active-red');
    updateLive();
}
function chA(d){la=Math.max(1,la+d);updateLive();}
function chB(d){lb=Math.max(1,lb+d);updateLive();}
function updateLive(){
    let c=Math.sqrt(la*la+lb*lb);
    document.getElementById('liveA').textContent='a = '+la;
    document.getElementById('liveB').textContent='b = '+lb;
    document.getElementById('liveForm').textContent=la+'² + '+lb+'² = '+c.toFixed(2)+'²';
    document.getElementById('liveDet').textContent='c = √('+(la*la)+'+'+(lb*lb)+') = '+c.toFixed(4);
}

function checkQuiz(i,ans,btn,n){
    document.querySelectorAll('#app .quiz-btn').forEach(b=>{b.disabled=true;b.classList.remove('correct','wrong');});
    if(i===ans){
        btn.classList.add('correct');
        document.getElementById('qf'+n).innerHTML='🎉 <b>آفرین! درسته!</b>';
        document.getElementById('qf'+n).style.color='#2ecc71';
    }else{
        btn.classList.add('wrong');
        document.getElementById('qf'+n).innerHTML='❌ اشتباه! گزینه صحیح '+String.fromCharCode(65+ans);
        document.getElementById('qf'+n).style.color='#e74c3c';
        document.querySelectorAll('#app .quiz-btn')[ans].classList.add('correct');
    }
}

// کیبورد
document.addEventListener('keydown',e=>{
    if(e.key==='ArrowRight'||e.key==='ArrowDown'){e.preventDefault();go(Math.min(55,cur+1));}
    if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();go(Math.max(1,cur-1));}
});

// شروع
render(1);
</script>
</body>
</html>"""

# ==========================================
# ذخیره و اجرا
# ==========================================
file_path = 'Pythagoras_55.html'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

webbrowser.open('file://' + os.path.abspath(file_path))

print("="*50)
print("✅ باز شد! ۵۵ اسلاید فیثاغورث")
print("="*50)
print("⌨ با کلیدهای ◀ ▶ حرکت کن")
print("🖱 روی دکمه‌ها کلیک کن")
