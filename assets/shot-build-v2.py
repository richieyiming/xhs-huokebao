# -*- coding: utf-8 -*-
"""天赋说明书获客包 · 6 张贴图 v2
升级点：原创几何符号系统 + 深色封面 + 点阵底纹 + 金色光晕 + 大字号水印 + 圆形节点
零命理符号：无罗盘/八卦/星象/掌纹/符咒，仅使用通用几何图形
"""
import pathlib

OUT = pathlib.Path("/tmp/tf-shots")
OUT.mkdir(parents=True, exist_ok=True)

CSS = """
:root{
  --bg:#FAF8F4; --panel:#FFFFFF; --ink:#1D1D1F; --sub:#6E6E73;
  --accent:#C9A84C; --accent2:#E8CE86; --accent-bg:#FBF6E9; --accent-ink:#8A6D1F;
  --line:#E8E5DE; --radius:18px; --dot:rgba(29,29,31,.085);
}
body.dark{
  --bg:#141416; --panel:#1B1B1E; --ink:#F6F3EB; --sub:#8B8781;
  --accent:#C9A84C; --accent2:#F0DEA3; --accent-bg:rgba(201,168,76,.13); --accent-ink:#E8CE86;
  --line:rgba(255,255,255,.13); --dot:rgba(201,168,76,.16);
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{margin:0;padding:0;background:#DCDCE1;
  font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Helvetica Neue",sans-serif}

.shot{
  width:1080px;height:1440px;background:var(--bg);position:relative;overflow:hidden;
  padding:104px 96px 200px;display:flex;flex-direction:column;
}
/* 顶部金色细线 */
.shot::before{content:'';position:absolute;top:0;left:0;width:100%;height:10px;
  background:linear-gradient(90deg,#C9A84C 0%,#E8CE86 46%,#C9A84C 100%)}
/* 点阵底纹 */
.deco{position:absolute;inset:0;pointer-events:none;
  background-image:radial-gradient(var(--dot) 1.7px,transparent 1.8px);background-size:38px 38px}
/* 金色光晕 */
.glow{position:absolute;inset:0;pointer-events:none}
.glow.a{background:radial-gradient(860px 700px at 76% -10%,rgba(201,168,76,.30),transparent 62%)}
.glow.b{background:radial-gradient(560px 560px at -8% 106%,rgba(201,168,76,.13),transparent 62%)}
/* 出血大圆环（右侧出画） */
.ring{position:absolute;right:-250px;top:250px;width:660px;height:660px;border-radius:50%;
  border:2px solid rgba(201,168,76,.20);pointer-events:none}
.ring.s{right:-140px;top:600px;width:280px;height:280px;border-color:rgba(201,168,76,.13)}
/* 超大水印序号 */
.soft .ghost{opacity:.028}
.ghost{position:absolute;right:44px;top:186px;font-size:400px;font-weight:800;color:var(--ink);
  opacity:.042;line-height:1;letter-spacing:-22px;pointer-events:none;user-select:none}

/* ---------- 页眉行 ---------- */
.head{display:flex;align-items:center;justify-content:space-between;
  padding-bottom:26px;border-bottom:2px solid var(--line);margin-bottom:54px;position:relative;z-index:2}
.head .left{display:flex;align-items:center;gap:22px}
.tag{font-size:32px;letter-spacing:4px;color:var(--accent-ink);font-weight:700}
.no{font-size:32px;color:var(--sub);font-weight:700;letter-spacing:3px;opacity:.8}

/* ---------- 标题区 ---------- */
h1{font-size:96px;line-height:1.28;letter-spacing:-2px;color:var(--ink);font-weight:800;
  margin-bottom:50px;position:relative;z-index:2}
h1 em{font-style:normal;color:var(--accent-ink);background:var(--accent-bg);padding:2px 14px;border-radius:10px}
.lead{font-size:45px;line-height:1.6;color:var(--sub);margin-bottom:52px;position:relative;z-index:2}

/* ---------- 列表 ---------- */
ul{list-style:none;margin-top:6px;position:relative;z-index:2}
li{font-size:51px;line-height:1.6;color:var(--ink);padding:30px 0;display:flex;gap:26px;align-items:flex-start}
li .tx{flex:1}
.bub{flex:0 0 auto;width:62px;height:62px;border-radius:50%;border:2.5px solid var(--accent);
  display:flex;align-items:center;justify-content:center;font-size:29px;font-weight:700;
  color:var(--accent-ink);margin-top:12px;background:var(--panel)}
.bub.x{border-color:rgba(201,168,76,.5);color:var(--accent);font-size:30px}
.bub.k{border-color:var(--accent);color:var(--accent-ink)}
.bub.tag2{width:auto;border-radius:14px;padding:0 20px;font-size:29px;height:58px}

/* ---------- 带竖向路径的列表（04 方法） ---------- */
ul.tl{margin-top:14px}
ul.tl::before{content:'';position:absolute;left:30px;top:71px;bottom:71px;width:2.5px;
  background:linear-gradient(180deg,var(--accent),rgba(201,168,76,.22))}
ul.tl li{padding:30px 0 30px 104px;display:block;position:relative}
ul.tl li .bub{position:absolute;left:0;top:50%;transform:translateY(-50%);margin-top:0}

/* ---------- 金句块 ---------- */
.quote{margin-top:auto;background:var(--accent-bg);border-left:11px solid var(--accent);
  padding:42px 40px;border-radius:0 var(--radius) var(--radius) 0;font-size:49px;line-height:1.5;
  color:var(--accent-ink);font-weight:700;position:relative;z-index:2}
.quote.fill{background:linear-gradient(135deg,#E6CE86 0%,#C9A84C 100%);border-left:0;border-radius:var(--radius);
  color:#221B06;text-align:center;font-size:46px}

/* ---------- 数据区 ---------- */
.statrow{display:flex;align-items:center;justify-content:space-between;gap:26px;
  margin:16px 0 22px;position:relative;z-index:2}
.bignum{font-size:198px;font-weight:800;line-height:1;letter-spacing:-6px;white-space:nowrap;
  background:linear-gradient(135deg,#8A6D1F 0%,#C9A84C 55%,#E8CE86 100%);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.statcap{font-size:60px;color:var(--sub);font-weight:700;margin-top:14px;letter-spacing:3px;white-space:nowrap}

/* ---------- 资料预览条 ---------- */
.getbar{display:flex;align-items:center;gap:22px;margin-top:20px;padding:26px 32px;
  border:2px dashed rgba(201,168,76,.55);border-radius:16px;background:var(--accent-bg);
  position:relative;z-index:2}
.getbar .t1{font-size:36px;font-weight:700;color:var(--accent-ink);line-height:1.3;letter-spacing:.5px}
.getbar .t2{font-size:32px;color:var(--sub);margin-top:7px;letter-spacing:1px}

/* ---------- 紧凑版（06 钩子：内容最多的那张） ---------- */
.tight .head{margin-bottom:44px}
.tight h1{margin-bottom:40px}
.tight .lead{margin-bottom:36px}
.tight li{padding:22px 0}
.tight .getbar{margin-top:16px;padding:24px 30px}
.tight .quote{padding:34px 32px;font-size:43px}

/* ---------- 落款 ---------- */
.base{position:absolute;left:96px;right:96px;bottom:178px;height:1.5px;
  background:linear-gradient(90deg,transparent,rgba(201,168,76,.42),transparent);pointer-events:none}
.foot{position:absolute;bottom:74px;left:96px;right:96px;font-size:32px;color:var(--sub);opacity:.72;
  display:flex;justify-content:space-between;letter-spacing:1px;z-index:2}

/* ================= 封面专用（居中海报式） ================= */
.cover{padding:104px 96px 200px;align-items:center;text-align:center}
.ctop{display:flex;align-items:center;gap:26px;margin-bottom:52px;position:relative;z-index:2}
.ctop i{display:block;width:56px;height:2px;background:rgba(201,168,76,.5)}
.ctop span{font-size:32px;letter-spacing:8px;color:var(--accent-ink);font-weight:700}
.emblem{margin:0 auto 42px;position:relative;z-index:2;display:flex;justify-content:center}
.cover h1{font-size:100px;line-height:1.26;letter-spacing:1px;margin-bottom:0;text-align:center}
.rule{width:150px;height:3px;background:var(--accent);margin:48px auto 44px;position:relative;z-index:2}
.cover .lead{margin-bottom:0;font-size:44px;text-align:center;letter-spacing:1px}
.cover .quote{align-self:stretch;text-align:left;font-size:47px;margin-top:auto}
body.dark .quote{border-left-color:var(--accent)}
"""

ACCOUNT = "一铭 · 天赋说明书"

# ============ 原创符号系统（纯几何，零命理） ============

def mark(name, size=54):
    """页眉迷你符号 54×54"""
    G = '#C9A84C'
    body = {
        # 1 光核：同心环 + 中心光点
        'core': f'<circle cx="27" cy="27" r="22" fill="none" stroke="{G}" stroke-opacity=".32" stroke-width="2.4"/>'
                f'<circle cx="27" cy="27" r="14" fill="none" stroke="{G}" stroke-opacity=".7" stroke-width="2.4"/>'
                f'<circle cx="27" cy="27" r="5" fill="{G}"/>',
        # 2 准星：定位十字
        'cross': f'<circle cx="27" cy="27" r="14.5" fill="none" stroke="{G}" stroke-opacity=".55" stroke-width="2.4"/>'
                 f'<path d="M27 3v12M27 39v12M3 27h12M39 27h12" fill="none" stroke="{G}" stroke-width="2.4" stroke-linecap="round"/>'
                 f'<circle cx="27" cy="27" r="4.2" fill="{G}"/>',
        # 3 断环：斜切圆环 = 走错的路
        'slash': f'<circle cx="27" cy="27" r="19" fill="none" stroke="{G}" stroke-opacity=".45" stroke-width="2.4"/>'
                 f'<path d="M14 40L40 14" fill="none" stroke="{G}" stroke-width="3.4" stroke-linecap="round"/>',
        # 4 阶梯路径：三段上升 + 节点
        'stairs': f'<path d="M5 46h13V32h14V18h15" fill="none" stroke="{G}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>'
                  f'<circle cx="18" cy="46" r="4" fill="{G}"/><circle cx="32" cy="32" r="4" fill="{G}"/><circle cx="47" cy="18" r="4" fill="{G}"/>',
        # 5 收敛线：五线汇聚一点
        'converge': f'<path d="M7 8L27 43M18 6L27 43M36 6L27 43M47 8L27 43" fill="none" stroke="{G}" '
                    f'stroke-width="2.4" stroke-linecap="round" stroke-opacity=".72"/>'
                    f'<circle cx="27" cy="46" r="5" fill="{G}"/>',
        # 6 信笺折角：卡片 + 折角
        'card': f'<rect x="6" y="11" width="42" height="34" rx="5" fill="none" stroke="{G}" stroke-width="2.4" stroke-opacity=".6"/>'
                f'<path d="M34 11l14 13" fill="none" stroke="{G}" stroke-width="2.2" stroke-linecap="round" stroke-opacity=".8"/>'
                f'<path d="M14 30h18M14 37h11" fill="none" stroke="{G}" stroke-width="2.6" stroke-linecap="round"/>',
    }[name]
    return f'<svg width="{size}" height="{size}" viewBox="0 0 54 54">{body}</svg>'


def emblem(size=222):
    """封面主视觉：光核（同心环 + 金色弧轨 + 位置点），纯几何构成"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 240 240">
<defs>
<linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="#F4E4AE"/><stop offset="100%" stop-color="#C9A84C"/></linearGradient>
</defs>
<circle cx="120" cy="120" r="115" fill="none" stroke="#C9A84C" stroke-opacity=".30" stroke-width="1.8"/>
<circle cx="120" cy="120" r="86" fill="none" stroke="#C9A84C" stroke-opacity=".36" stroke-width="2.2" stroke-dasharray="3 15"/>
<circle cx="120" cy="120" r="57" fill="none" stroke="url(#lg)" stroke-width="3.4"/>
<circle cx="120" cy="120" r="20" fill="url(#lg)"/>
<path d="M120 5A115 115 0 0 1 214.2 54" fill="none" stroke="url(#lg)" stroke-width="5.5" stroke-linecap="round"/>
<circle cx="214.2" cy="54" r="7.5" fill="url(#lg)"/>
</svg>'''


def converge_art(size=250):
    """案例页配图：宽口收拢到一点 + 收拢点光环"""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 200 200">
<defs><linearGradient id="cg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#C9A84C" stop-opacity=".28"/><stop offset="100%" stop-color="#C9A84C" stop-opacity=".85"/>
</linearGradient></defs>
<path d="M16 18L100 150M52 12L100 150M148 12L100 150M184 18L100 150" fill="none"
  stroke="url(#cg)" stroke-width="3.2" stroke-linecap="round"/>
<circle cx="100" cy="152" r="17" fill="none" stroke="#C9A84C" stroke-opacity=".40" stroke-width="2.4"/>
<circle cx="100" cy="152" r="8" fill="#C9A84C"/>
<path d="M16 18h168" stroke="#C9A84C" stroke-opacity=".42" stroke-width="1.8" stroke-dasharray="7 9"/>
</svg>'''


SHOTS = []

# ---------------- 01 封面（深色海报） ----------------
SHOTS.append(("dark", "cover", f"""  <div class="deco"></div>
  <div class="glow a"></div><div class="glow b"></div>
  <div class="ring"></div><div class="ring s"></div>
  <div class="ctop"><i></i><span>天赋说明书 · 优势自测</span><i></i></div>
  <div class="emblem">{emblem()}</div>
  <h1>工作了5年<br>还是不知道<br>自己<em>适合什么</em></h1>
  <div class="rule"></div>
  <div class="lead">不是你不行，是没人告诉你该往哪儿使劲</div>
  <div class="quote">你自己就是答案<br>只是从没人帮你把它写下来</div>"""))

# ---------------- 02 痛点（准星） ----------------
SHOTS.append(("", "", f"""  <div class="deco"></div><div class="glow a"></div>
  <div class="ghost">02</div>
  <div class="head"><div class="left">{mark('cross')}<span class="tag">痛点 · 共情卡</span></div><span class="no">02</span></div>
  <h1>是不是<br>也这样？</h1>
  <ul>
    <li><span class="bub">1</span><span class="tx">问你擅长什么，你答不上来</span></li>
    <li><span class="bub">2</span><span class="tx">课报了不少，还是不知往哪用</span></li>
    <li><span class="bub">3</span><span class="tx">每天都很忙，忙完更空</span></li>
  </ul>
  <div class="quote">不是你不努力，是你一直在没有方向地使劲</div>"""))

# ---------------- 03 拆解（断环） ----------------
SHOTS.append(("", "", f"""  <div class="deco"></div><div class="glow a"></div>
  <div class="ghost">03</div>
  <div class="head"><div class="left">{mark('slash')}<span class="tag">拆解 · 认知卡</span></div><span class="no">03</span></div>
  <h1>为什么<br>你之前没做成</h1>
  <ul>
    <li><span class="bub x">✕</span><span class="tx">什么都学一点，就都是皮毛</span></li>
    <li><span class="bub x">✕</span><span class="tx">先干着，方向以后再想</span></li>
    <li><span class="bub x">✕</span><span class="tx">别人能成，我也能成</span></li>
  </ul>
  <div class="quote">天赋不是「我比别人强」，是「我做什么不费劲」</div>"""))

# ---------------- 04 方法（阶梯路径） ----------------
SHOTS.append(("", "", f"""  <div class="deco"></div><div class="glow a"></div>
  <div class="ghost">04</div>
  <div class="head"><div class="left">{mark('stairs')}<span class="tag">方法 · 干货卡</span></div><span class="no">04</span></div>
  <h1>正确的<br>顺序是这样</h1>
  <ul class="tl">
    <li><span class="bub">1</span><span class="tx">写出3件做得格外顺手的事</span></li>
    <li><span class="bub">2</span><span class="tx">找出这3件事的共性</span></li>
    <li><span class="bub">3</span><span class="tx">把共性变成动作，去选下一步</span></li>
  </ul>
  <div class="quote">第③步最难，我把它整理成了《自测7问》</div>"""))

# ---------------- 05 案例（收敛线） ----------------
SHOTS.append(("", "soft", f"""  <div class="deco"></div><div class="glow a"></div><div class="glow b"></div>
  <div class="ghost">05</div>
  <div class="head"><div class="left">{mark('converge')}<span class="tag">案例 · 证据卡</span></div><span class="no">05</span></div>
  <h1>我做对了哪一步</h1>
  <div class="statrow">
    <div class="stat">
      <div class="bignum">90%</div>
      <div class="statcap">的精力</div>
    </div>
    {converge_art(268)}
  </div>
  <ul>
    <li><span class="bub tag2">前</span><span class="tx">什么都想学，样样开了个头</span></li>
    <li><span class="bub tag2">后</span><span class="tx">五年只压一个交叉点</span></li>
  </ul>
  <div class="quote">没有奇迹，只是把力气用对了地方</div>"""))

# ---------------- 06 钩子（信笺 + 金色 CTA） ----------------
SHOTS.append(("", "tight", f"""  <div class="deco"></div><div class="glow a"></div>
  <div class="ghost">06</div>
  <div class="head"><div class="left">{mark('card')}<span class="tag">钩子 · 行动卡</span></div><span class="no">06</span></div>
  <h1>评论区<em>扣【天赋】</em></h1>
  <div class="lead">整理好的《自测7问》PDF，发你</div>
  <ul>
    <li><span class="bub k">✓</span><span class="tx">五个板块的自测问题</span></li>
    <li><span class="bub k">✓</span><span class="tx">两个「假天赋」的坑</span></li>
    <li><span class="bub k">✓</span><span class="tx">我自己的答案样例</span></li>
  </ul>
  <div class="getbar">{mark('card', 46)}<div><div class="t1">《天赋说明书 · 自测7问》</div><div class="t2">PDF 资料 · 看清楚自己再决定要不要改</div></div></div>
  <div class="quote fill">先别急着改自己，先把自己看清楚</div>"""))

TPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="UTF-8"><title>shot-{no}</title><style>{css}</style></head>
<body class="{cls}">
<section class="shot {extra}">
{body}
  <div class="base"></div>
  <div class="foot"><span>{acct}</span><span>{no} / 06</span></div>
</section>
</body>
</html>
"""

for i, (cls, extra, body) in enumerate(SHOTS, 1):
    no = "%02d" % i
    cls = ("t-knowledge " + cls).strip()
    html = TPL.format(no=no, css=CSS, body=body, acct=ACCOUNT, cls=cls, extra=extra)
    (OUT / ("v2-%s.html" % no)).write_text(html, encoding="utf-8")

print("built", len(SHOTS), "->", OUT)
