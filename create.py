html = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>민주의 우정 정원 🌸</title>
<link href="https://fonts.googleapis.com/css2?family=Gaegu:wght@400;700&family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet">
<style>
:root {
  --pink1: #D63F82;
  --pink2: #EF7FAD;
  --pink3: #F8C0D8;
  --pink4: #FEF0F8;
  --lav1: #6D28D9;
  --lav2: #A07FE8;
  --lav3: #EDE4FF;
  --mint1: #0D9488;
  --mint2: #5EEAD4;
  --mint3: #CCFBF1;
  --yel1: #B45309;
  --yel2: #FEF3C7;
  --peach: #EA7A42;
  --coral: #DC4B2C;
  --white: #FFFFFF;
  --cream: #FFFBF5;
  --text: #1A0A22;
  --text2: #3D1A52;
  --muted: #5E3A70;
  --border: #C8A0D8;
  --shadow: rgba(110,30,90,0.18);
  --i-col: #1D4ED8;
  --e-col: #B45309;
  --bridge-col: #6D28D9;
  --played-col: #0F766E;
  --ext-col: #B45309;
  --best-col: #D63F82;
  --friend-col: #6D28D9;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Noto Sans KR', sans-serif;
  background: var(--cream);
  color: var(--text);
  min-height: 100vh;
  overflow-x: hidden;
  font-size: 14px;
  background-image: radial-gradient(circle at 15% 10%, #FFE4F3 0%, transparent 40%),
    radial-gradient(circle at 85% 5%, #EDE0FF 0%, transparent 35%),
    radial-gradient(circle at 50% 95%, #E0F9F3 0%, transparent 40%);
}
#petalCanvas { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
.app { position: relative; z-index: 1; max-width: 520px; margin: 0 auto; }

/* HEADER */
.header {
  padding: 20px 20px 16px;
  background: linear-gradient(135deg, #D63F82, #7C3AED, #0D9488);
  text-align: center;
  position: relative;
  overflow: hidden;
  border-bottom: 3px solid var(--pink2);
}
.header::before { content: '🌸✨💫🌷✨🌸💫🌷✨🌸💫🌷'; position: absolute; top: 5px; left: 0; right: 0; font-size: 12px; letter-spacing: 4px; opacity: .7; }
.header::after  { content: '🌸✨💫🌷✨🌸💫🌷✨🌸💫🌷'; position: absolute; bottom: 5px; left: 0; right: 0; font-size: 12px; letter-spacing: 4px; opacity: .5; }
.header-title { font-family: 'Gaegu', cursive; font-size: 30px; font-weight: 700; color: var(--white); text-shadow: 2px 3px 0 rgba(80,10,60,.4), 0 0 20px rgba(255,255,255,.5); position: relative; letter-spacing: 1px; }
.header-sub { font-size: 13px; color: rgba(255,255,255,.95); font-weight: 700; margin-top: 4px; position: relative; }

/* HUD */
.hud { display: flex; background: white; border-bottom: 3px solid var(--pink2); position: sticky; top: 0; z-index: 100; box-shadow: 0 3px 16px var(--shadow); overflow: hidden; }
.hb { flex: 1; padding: 8px 4px; text-align: center; border-right: 2px solid var(--border); min-width: 0; overflow: hidden; }
.hb:last-child { border-right: none; }
.hl { font-size: 10px; color: var(--muted); font-weight: 900; text-transform: uppercase; letter-spacing: .5px; }
.hv { font-family: 'Gaegu', cursive; font-size: 24px; color: var(--pink1); line-height: 1.1; }
.hv.t { color: var(--mint1); }
.hv.r { color: var(--coral); }
.lpill { display: inline-flex; align-items: center; background: linear-gradient(135deg, var(--pink2), var(--lav2)); border-radius: 20px; padding: 3px 11px; font-size: 11px; font-weight: 900; color: var(--text); margin-top: 2px; border: 2px solid var(--white); box-shadow: 0 2px 8px var(--shadow); }

/* XP BAR */
.xpw { padding: 5px 10px 9px; background: white; border-bottom: 1px solid var(--border); }
.xpb { height: 9px; background: var(--pink3); border-radius: 20px; overflow: hidden; }
.xpf { height: 100%; border-radius: 20px; background: linear-gradient(90deg, var(--pink1), var(--lav1), var(--mint1)); transition: width .6s; box-shadow: 0 0 8px var(--pink2); }

/* TABS */
.tabs { display: flex; background: white; border-bottom: 3px solid var(--pink2); overflow-x: auto; scrollbar-width: none; }
.tabs::-webkit-scrollbar { display: none; }
.tab { flex-shrink: 0; padding: 11px 14px; font-size: 12px; font-weight: 900; color: var(--muted); border: none; background: none; cursor: pointer; border-bottom: 3px solid transparent; margin-bottom: -3px; transition: all .2s; font-family: 'Noto Sans KR', sans-serif; }
.tab.active { color: var(--pink1); border-bottom-color: var(--pink1); }
.tab:hover { color: var(--text2); }

.content { padding: 12px; }
.panel { display: none; }
.panel.active { display: block; }

/* CARDS */
.qc { background: white; border-radius: 20px; padding: 16px 18px; margin-bottom: 12px; border: 2.5px solid var(--border); box-shadow: 0 4px 20px var(--shadow); position: relative; overflow: hidden; }
.qc::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 5px; background: linear-gradient(90deg, var(--pink1), var(--lav1), var(--mint1)); border-radius: 20px 20px 0 0; }
.qc.lavender { border-color: var(--lav2); }
.qc.lavender::before { background: linear-gradient(90deg, var(--lav1), var(--pink1)); }
.qc.mint { border-color: var(--mint2); }
.qc.mint::before { background: linear-gradient(90deg, var(--mint1), var(--lav1)); }
.qc.peach { border-color: #E8A880; }
.qc.peach::before { background: linear-gradient(90deg, var(--peach), var(--pink1)); }

.ch { font-family: 'Gaegu', cursive; font-size: 18px; font-weight: 700; color: var(--pink1); margin-bottom: 10px; display: flex; align-items: center; gap: 7px; }

/* PROGRESS */
.pgr { margin-bottom: 8px; }
.pgl { display: flex; justify-content: space-between; font-size: 11px; color: var(--text2); font-weight: 700; margin-bottom: 5px; }
.pgb { height: 11px; background: var(--pink3); border-radius: 20px; overflow: hidden; }
.pgf { height: 100%; border-radius: 20px; background: linear-gradient(90deg, var(--pink1), var(--lav1)); box-shadow: 0 0 8px var(--pink2); transition: width .5s; }

/* BUTTONS */
.rbtn { width: 100%; padding: 15px; background: linear-gradient(135deg, var(--pink1), var(--lav1)); border: none; border-radius: 16px; color: white; font-family: 'Gaegu', cursive; font-size: 17px; font-weight: 700; cursor: pointer; margin-bottom: 12px; transition: all .2s; box-shadow: 0 4px 16px rgba(214,63,130,.4); position: relative; }
.rbtn:hover { transform: translateY(-2px); box-shadow: 0 7px 22px rgba(214,63,130,.5); }
.rbtn::after { content: '🌸'; position: absolute; right: 16px; top: 50%; transform: translateY(-50%); font-size: 18px; }

/* FORM */
.fp { background: var(--pink4); border: 2.5px solid var(--pink3); border-radius: 18px; padding: 16px; margin-bottom: 12px; }
.fl { font-size: 11px; color: var(--text2); font-weight: 900; text-transform: uppercase; letter-spacing: .8px; margin-bottom: 5px; display: block; }
.fi { width: 100%; padding: 10px 13px; background: white; border: 2px solid var(--border); border-radius: 12px; color: var(--text); font-family: 'Noto Sans KR', sans-serif; font-size: 14px; outline: none; transition: all .2s; margin-bottom: 10px; }
.fi:focus { border-color: var(--pink1); box-shadow: 0 0 12px rgba(214,63,130,.2); }
.frow { display: flex; gap: 8px; }
.frow .fg { flex: 1; }
.fg { margin-bottom: 10px; }
.fsel { width: 100%; padding: 10px 13px; background: white; border: 2px solid var(--border); border-radius: 12px; color: var(--text); font-family: 'Noto Sans KR', sans-serif; font-size: 14px; outline: none; cursor: pointer; }

/* CHIPS */
.chips { display: flex; flex-wrap: wrap; gap: 6px; }
.chip { padding: 6px 13px; border-radius: 20px; border: 2px solid var(--border); background: white; color: var(--text2); font-size: 12px; font-weight: 700; cursor: pointer; transition: all .15s; font-family: 'Noto Sans KR', sans-serif; }
.chip.on { background: linear-gradient(135deg, var(--pink1), var(--lav1)); color: white; border-color: var(--pink1); box-shadow: 0 2px 10px rgba(214,63,130,.4); }
.chip:hover { border-color: var(--pink1); color: var(--pink1); }

.sbtn { width: 100%; padding: 13px; background: linear-gradient(135deg, var(--pink1), var(--lav1)); border: none; border-radius: 14px; color: white; font-family: 'Gaegu', cursive; font-size: 17px; font-weight: 700; cursor: pointer; margin-top: 6px; box-shadow: 0 4px 14px rgba(214,63,130,.4); }
.cbtn { width: 100%; padding: 10px; background: white; border: 2px solid var(--border); border-radius: 12px; color: var(--muted); font-size: 12px; cursor: pointer; margin-top: 5px; font-family: 'Noto Sans KR', sans-serif; font-weight: 700; }

/* FILTER BAR */
.fbar { display: flex; gap: 5px; flex-wrap: wrap; margin-bottom: 10px; }
.fc { padding: 6px 13px; border-radius: 20px; border: 2px solid var(--border); background: white; color: var(--muted); font-size: 11px; font-weight: 700; cursor: pointer; transition: all .15s; font-family: 'Noto Sans KR', sans-serif; }
.fc.on { background: var(--pink1); color: white; border-color: var(--pink1); }

/* ALLY LIST */
.alist { display: flex; flex-direction: column; gap: 8px; }
.acard { background: white; border: 2px solid var(--border); border-radius: 16px; padding: 13px 15px; display: flex; gap: 11px; align-items: center; cursor: pointer; transition: all .2s; flex-direction: column; }
.acard:hover { border-color: var(--pink1); box-shadow: 0 6px 20px var(--shadow); }
.acard.ext-c { border-color: #D4B060; background: #FFFDF0; }
.acard.ext-c:hover { border-color: var(--yel1); box-shadow: 0 4px 16px rgba(180,83,9,.2); }

/* AVATAR */
.av { width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; flex-shrink: 0; position: relative; }
.ar { position: absolute; inset: -3px; border-radius: 50%; border: 2.5px solid transparent; }
.ar-i { border-color: var(--i-col); box-shadow: 0 0 8px rgba(29,78,216,.4); }
.ar-e { border-color: var(--e-col); box-shadow: 0 0 8px rgba(180,83,9,.4); }
.ar-b { border-color: var(--bridge-col); box-shadow: 0 0 10px rgba(109,40,217,.5); }
.ar-p { border-color: var(--played-col); box-shadow: 0 0 10px rgba(13,148,136,.5); }
.ar-x { border-color: var(--yel1); box-shadow: 0 0 10px rgba(180,83,9,.4); border-style: dashed; }
.ar-drifting { border-color: var(--e-col); box-shadow: 0 0 8px rgba(180,83,9,.3); border-style: dashed; }
.ar-distant { border-color: var(--lav2); box-shadow: 0 0 6px rgba(160,127,232,.3); border-style: dotted; opacity: .7; }

.ai { flex: 1; min-width: 0; }
.an { font-weight: 900; font-size: 14px; color: var(--text); }
.atg { display: flex; gap: 4px; flex-wrap: wrap; margin-top: 4px; }

/* BADGES */
.bdg { font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 20px; border: 1.5px solid; }
.bi  { color: var(--i-col); border-color: var(--i-col); background: rgba(29,78,216,.10); }
.be  { color: var(--e-col); border-color: var(--e-col); background: rgba(180,83,9,.10); }
.bb  { color: var(--bridge-col); border-color: var(--bridge-col); background: rgba(109,40,217,.12); }
.bq  { color: #4A2A55; border-color: #A070B0; background: rgba(160,130,170,.12); }
.bc  { color: var(--coral); border-color: var(--coral); background: rgba(220,75,44,.10); }
.bs  { color: var(--mint1); border-color: var(--mint1); background: rgba(13,148,136,.12); }
.bp  { color: #0F766E; border-color: var(--mint1); background: rgba(13,148,136,.15); }
.bl  { color: var(--best-col); border-color: var(--pink1); background: rgba(214,63,130,.10); }
.bx  { color: var(--yel1); border-color: var(--yel1); background: rgba(180,83,9,.12); }
.bldr{ color: var(--lav1); border-color: var(--lav1); background: rgba(109,40,217,.10); }
.alk { font-size: 11px; color: var(--muted); margin-top: 3px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

/* DIVIDER */
.sdiv { display: flex; align-items: center; gap: 7px; margin: 13px 0 7px; font-size: 11px; font-weight: 900; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }
.sdiv::before, .sdiv::after { content: ''; flex: 1; height: 1.5px; background: var(--border); }

.empty { text-align: center; padding: 30px 20px; color: var(--muted); }
.empty .ico { font-size: 40px; margin-bottom: 10px; }
.empty p { font-size: 13px; line-height: 1.8; font-weight: 700; }

/* MAP */
.view-toggle { display: flex; gap: 5px; margin-bottom: 9px; }
.vtbtn { flex: 1; padding: 8px; border-radius: 12px; border: 2px solid var(--border); background: white; color: var(--muted); font-size: 11px; font-weight: 700; cursor: pointer; transition: all .15s; font-family: 'Noto Sans KR', sans-serif; text-align: center; }
.vtbtn.on { background: linear-gradient(135deg, var(--pink2), var(--lav2)); color: var(--text); border-color: var(--pink1); }
.map-toolbar { display: flex; gap: 5px; flex-wrap: wrap; margin-bottom: 9px; }
.mtool { padding: 6px 13px; border-radius: 20px; border: 2px solid var(--border); background: white; color: var(--muted); font-size: 11px; font-weight: 700; cursor: pointer; transition: all .15s; font-family: 'Noto Sans KR', sans-serif; }
.mtool.on { background: var(--pink1); color: white; border-color: var(--pink1); }
#mapCanvas { width: 100%; border-radius: 16px; cursor: pointer; display: block; }
.map-hint { font-size: 11px; color: var(--muted); text-align: center; margin-top: 5px; font-weight: 700; }
.map-legend { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 9px; }
.mleg { display: flex; align-items: center; gap: 4px; font-size: 10px; color: var(--text2); font-weight: 700; }
.mld { width: 10px; height: 10px; border-radius: 50%; }
.mll { width: 18px; height: 2px; border-radius: 1px; }

/* RELATION EDITOR */
.rel-ed { background: var(--lav3); border: 2px solid var(--lav2); border-radius: 14px; padding: 12px; margin-top: 9px; }
.re-title { font-family: 'Gaegu', cursive; font-size: 15px; color: var(--lav1); margin-bottom: 8px; }
.re-chips { display: flex; gap: 6px; flex-wrap: wrap; }
.rc { padding: 7px 15px; border-radius: 20px; border: 2px solid var(--border); background: white; color: var(--text2); font-size: 12px; font-weight: 700; cursor: pointer; font-family: 'Noto Sans KR', sans-serif; transition: all .15s; }
.rc:hover { border-color: var(--pink1); }
.rc.best { background: linear-gradient(135deg, var(--pink2), var(--yel2)); color: var(--text); border-color: var(--pink1); }
.rc.friend { background: linear-gradient(135deg, var(--lav2), var(--mint2)); color: var(--text); border-color: var(--lav1); }
.rc.gone { background: #FFF0F0; color: #CC4040; border-color: #FF9090; }

/* STATS */
.stat-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; }
.sg { background: var(--pink4); padding: 10px 5px; border-radius: 12px; text-align: center; border: 2px solid var(--pink3); }
.sg .sv { font-family: 'Gaegu', cursive; font-size: 20px; }
.sg .sk { font-size: 10px; color: var(--muted); margin-top: 1px; font-weight: 700; }

/* STRATEGY */
.strat-row { background: var(--lav3); border: 2px solid var(--lav2); border-radius: 14px; padding: 12px; margin-bottom: 8px; display: flex; gap: 11px; align-items: flex-start; }
.snum { width: 34px; height: 34px; border-radius: 50%; background: linear-gradient(135deg, var(--pink1), var(--lav1)); color: white; font-family: 'Gaegu', cursive; font-size: 17px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 3px 8px var(--shadow); }
.stit { font-weight: 900; font-size: 13px; color: var(--text); margin-bottom: 3px; }
.sdsc { font-size: 11px; color: var(--text2); line-height: 1.7; }
.sex { background: white; border-radius: 9px; padding: 5px 10px; margin-top: 5px; font-size: 11px; color: var(--pink1); font-weight: 700; border: 1.5px solid var(--pink3); }

/* BRIDGE PATH */
.bpath { display: flex; align-items: center; flex-wrap: wrap; gap: 4px; padding: 6px 0; overflow-x: auto; -webkit-overflow-scrolling: touch; }
.pn { padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: 700; }
.pj { background: var(--pink3); border: 1.5px solid var(--pink1); color: var(--pink1); }
.pe { background: var(--yel2); border: 1.5px solid var(--yel1); color: var(--yel1); }
.pb { background: var(--lav3); border: 1.5px solid var(--lav1); color: var(--lav1); }
.pf { background: var(--mint3); border: 1.5px solid var(--mint1); color: #0D6560; }
.pa { color: var(--muted); font-size: 14px; }

/* MODAL */
.moverlay { display: none; position: fixed; inset: 0; background: rgba(80,10,60,.45); z-index: 200; align-items: flex-end; justify-content: center; padding: 6px 6px 0 6px; backdrop-filter: blur(4px); }
.moverlay.open { display: flex; }
.mbox { background: white; border: 3px solid var(--pink2); border-radius: 24px 24px 16px 16px; width: 100%; max-width: 480px; max-height: 90vh; overflow-y: auto; padding: 18px; box-shadow: 0 -8px 40px rgba(214,63,130,.3); }
.mbox::before { content: ''; display: block; width: 100%; height: 5px; background: linear-gradient(90deg, var(--pink1), var(--lav1), var(--mint1)); border-radius: 10px; margin-bottom: 16px; }
.mtop { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
.mname { font-family: 'Gaegu', cursive; font-size: 23px; color: var(--text); }
.mcls { background: var(--pink3); border: none; color: var(--pink1); border-radius: 50%; width: 32px; height: 32px; cursor: pointer; font-size: 15px; font-weight: 700; }
.mrow { display: flex; gap: 7px; margin-bottom: 8px; align-items: flex-start; }
.mlbl { font-size: 10px; color: var(--muted); font-weight: 700; width: 60px; flex-shrink: 0; padding-top: 2px; }
.mval { font-size: 13px; color: var(--text); flex: 1; line-height: 1.6; }

/* ACTION GRID */
.agrid { display: grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-top: 10px; }
.act { padding: 10px; border-radius: 12px; border: 2px solid var(--border); background: var(--pink4); color: var(--muted); font-size: 11px; font-weight: 700; cursor: pointer; transition: all .15s; font-family: 'Noto Sans KR', sans-serif; text-align: center; }
.act:hover { border-color: var(--pink1); color: var(--text); }
.act.on { background: linear-gradient(135deg, var(--pink1), var(--lav1)); color: white; border-color: var(--pink1); }
.act.on-t { background: var(--mint3); color: #065F52; border-color: var(--mint1); font-weight: 900; }
.act.on-g { background: var(--lav3); color: var(--lav1); border-color: var(--lav2); font-weight: 900; }

.delbtn { width: 100%; margin-top: 10px; padding: 10px; background: white; border: 2px solid #FFAAAA; color: #CC3333; border-radius: 12px; font-size: 12px; cursor: pointer; font-family: 'Noto Sans KR', sans-serif; font-weight: 700; }

/* MISSIONS */
.msn { background: white; border: 2px solid var(--border); border-radius: 16px; padding: 14px 16px; margin-bottom: 9px; position: relative; overflow: hidden; }
.msn::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 5px; border-radius: 4px 0 0 4px; }
.msn.daily::before  { background: linear-gradient(180deg, var(--pink1), var(--pink2)); }
.msn.social::before { background: linear-gradient(180deg, var(--mint1), var(--mint2)); }
.msn.brave::before  { background: linear-gradient(180deg, var(--lav1), var(--lav2)); }
.msn.done { opacity: .5; }
.msn.done .mtit { text-decoration: line-through; }
.mtr { display: flex; justify-content: space-between; align-items: flex-start; }
.mtit { font-weight: 900; font-size: 13px; color: var(--text); margin-bottom: 5px; }
.mdsc { font-size: 11px; color: var(--text2); line-height: 1.7; }
.xtg { display: inline-flex; align-items: center; background: var(--pink3); border: 1.5px solid var(--pink2); color: var(--pink1); padding: 3px 9px; border-radius: 20px; font-size: 11px; font-weight: 900; margin-top: 6px; }
.dbtn { padding: 8px 15px; background: linear-gradient(135deg, var(--pink1), var(--lav1)); border: none; border-radius: 20px; color: white; font-size: 11px; font-weight: 900; cursor: pointer; white-space: nowrap; font-family: 'Noto Sans KR', sans-serif; flex-shrink: 0; margin-left: 7px; box-shadow: 0 3px 10px var(--shadow); }
.dbtn:disabled { background: var(--pink3); color: var(--muted); cursor: default; box-shadow: none; }

/* LEVEL */
.lvrow { display: flex; align-items: center; gap: 9px; padding: 10px 0; border-bottom: 1.5px solid var(--border); }
.lvrow:last-child { border-bottom: none; }
.lvic { font-size: 24px; width: 32px; text-align: center; }
.lvi { flex: 1; }
.lvn { font-weight: 900; font-size: 13px; color: var(--text); }
.lvr { font-size: 11px; color: var(--muted); font-weight: 700; }
.lvc { font-size: 11px; color: var(--pink1); font-weight: 900; }

/* TOAST */
.toast { position: fixed; bottom: 22px; left: 50%; transform: translateX(-50%) translateY(80px); background: linear-gradient(135deg, var(--pink1), var(--lav1)); color: white; padding: 12px 24px; border-radius: 28px; font-weight: 900; font-size: 13px; box-shadow: 0 6px 24px rgba(214,63,130,.5); z-index: 9999; transition: transform .3s; white-space: nowrap; border: 2px solid white; }
.toast.show { transform: translateX(-50%) translateY(0); }

@keyframes floatUp { 0% { transform: translateY(0) scale(1); opacity: 1; } 100% { transform: translateY(-55px) scale(.5); opacity: 0; } }
.xpfl { position: fixed; pointer-events: none; z-index: 9998; font-family: 'Gaegu', cursive; font-size: 18px; color: var(--pink1); animation: floatUp 1.2s ease forwards; text-shadow: 0 0 8px var(--pink2); }

/* EDIT FORM */
.efi { width: 100%; padding: 9px 12px; background: var(--pink4); border: 2px solid var(--pink3); border-radius: 10px; color: var(--text); font-family: 'Noto Sans KR', sans-serif; font-size: 14px; outline: none; margin-bottom: 8px; transition: border-color .2s; resize: vertical; min-height: 38px; }
.efi:focus { border-color: var(--pink1); }
.efl { font-size: 11px; color: var(--text2); font-weight: 900; text-transform: uppercase; letter-spacing: .8px; margin-bottom: 4px; display: block; }
.esavebtn { width: 100%; padding: 12px; background: linear-gradient(135deg, var(--pink1), var(--lav1)); border: none; border-radius: 12px; color: white; font-family: 'Gaegu', cursive; font-size: 16px; cursor: pointer; margin-top: 4px; box-shadow: 0 3px 10px var(--shadow); }
.ecancelbtn { width: 100%; padding: 9px; background: white; border: 2px solid var(--border); border-radius: 10px; color: var(--muted); font-size: 12px; cursor: pointer; margin-top: 5px; font-family: 'Noto Sans KR', sans-serif; font-weight: 700; }
.editbtn { padding: 8px 15px; background: var(--lav3); border: 2px solid var(--lav2); border-radius: 20px; color: var(--lav1); font-size: 11px; font-weight: 700; cursor: pointer; font-family: 'Noto Sans KR', sans-serif; }

/* MODAL TABS */
.mtab-row { display: flex; gap: 4px; margin-bottom: 14px; background: var(--pink4); border-radius: 14px; padding: 4px; }
.mtab { flex: 1; padding: 8px 4px; border-radius: 10px; border: none; background: none; font-size: 11px; font-weight: 900; color: var(--muted); cursor: pointer; font-family: 'Noto Sans KR', sans-serif; transition: all .15s; text-align: center; }
.mtab.on { background: white; color: var(--pink1); box-shadow: 0 2px 8px var(--shadow); }

/* MIND GAME */
.mgame { background: white; border-radius: 20px; padding: 16px 18px; margin-bottom: 12px; border: 2.5px solid var(--border); box-shadow: 0 4px 20px var(--shadow); }
.mgame::before { content: ''; display: block; height: 5px; background: linear-gradient(90deg, var(--lav1), var(--pink1), var(--mint1)); border-radius: 10px; margin-bottom: 12px; }
.scene-box { background: linear-gradient(135deg, var(--pink4), var(--lav3)); border: 2px solid var(--lav2); border-radius: 14px; padding: 14px; margin-bottom: 12px; text-align: center; }
.scene-emoji { font-size: 40px; display: block; margin-bottom: 6px; }
.scene-title { font-family: 'Gaegu', cursive; font-size: 18px; color: var(--text); margin-bottom: 4px; }
.scene-desc { font-size: 12px; color: var(--text2); line-height: 1.7; }
.think-label { font-size: 11px; font-weight: 900; color: var(--pink1); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
.think-options { display: flex; flex-direction: column; gap: 7px; margin-bottom: 12px; }
.topt { padding: 11px 14px; border-radius: 12px; border: 2px solid var(--border); background: white; color: var(--text); font-size: 13px; font-weight: 700; cursor: pointer; text-align: left; transition: all .2s; font-family: 'Noto Sans KR', sans-serif; display: flex; align-items: center; gap: 8px; }
.topt:hover { border-color: var(--pink1); background: var(--pink4); }
.topt.selected-good { border-color: var(--mint1); background: var(--mint3); color: #065F52; }
.topt.selected-bad  { border-color: var(--lav1);  background: var(--lav3);  color: var(--text2); }
.topt-num { width: 26px; height: 26px; border-radius: 50%; background: var(--pink3); color: var(--pink1); font-size: 12px; font-weight: 900; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.result-box { background: linear-gradient(135deg, var(--mint3), var(--lav3)); border: 2px solid var(--mint2); border-radius: 14px; padding: 14px; display: none; }
.result-box.show { display: block; }
.result-title { font-family: 'Gaegu', cursive; font-size: 17px; color: var(--mint1); margin-bottom: 6px; }
.result-msg { font-size: 12px; color: var(--text2); line-height: 1.7; }
.result-star { font-size: 30px; text-align: center; margin-bottom: 6px; }
.next-btn { width: 100%; padding: 12px; background: linear-gradient(135deg, var(--lav1), var(--pink1)); border: none; border-radius: 12px; color: white; font-family: 'Gaegu', cursive; font-size: 16px; cursor: pointer; margin-top: 10px; }
.game-progress { display: flex; gap: 5px; justify-content: center; margin-bottom: 10px; }
.gpdot { width: 11px; height: 11px; border-radius: 50%; background: var(--border); transition: background .3s; }
.gpdot.done { background: var(--pink1); }
.gpdot.cur  { background: var(--lav1); box-shadow: 0 0 6px var(--lav1); }
.score-banner { text-align: center; padding: 11px; background: linear-gradient(135deg, var(--pink3), var(--lav2)); border-radius: 14px; margin-bottom: 10px; }
.score-banner .sb { font-family: 'Gaegu', cursive; font-size: 23px; color: var(--text); }
.score-banner .sl { font-size: 12px; color: var(--text2); font-weight: 700; }

/* DETECTIVE */
.det-card { background: white; border: 2.5px solid var(--border); border-radius: 18px; padding: 16px 18px; margin-bottom: 12px; overflow: hidden; position: relative; }
.det-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 5px; background: linear-gradient(90deg, var(--lav1), var(--mint1)); }
.det-q { font-family: 'Gaegu', cursive; font-size: 16px; color: var(--text); margin-bottom: 10px; line-height: 1.5; }
.det-situation { background: linear-gradient(135deg, var(--pink4), var(--lav3)); border-radius: 12px; padding: 11px 14px; font-size: 13px; color: var(--text2); margin-bottom: 12px; border: 1.5px solid var(--pink3); line-height: 1.7; }
.det-options { display: flex; flex-direction: column; gap: 7px; }
.det-opt { background: white; border: 2px solid var(--border); border-radius: 12px; padding: 11px 14px; font-size: 13px; color: var(--text2); cursor: pointer; transition: all .2s; text-align: left; font-family: 'Noto Sans KR', sans-serif; line-height: 1.5; font-weight: 700; }
.det-opt:hover { border-color: var(--pink1); background: var(--pink4); color: var(--text); }
.det-opt.picked-good { background: linear-gradient(135deg, var(--mint3), var(--lav3)); border-color: var(--mint1); color: #065F52; }
.det-opt.picked-ok   { background: var(--lav3); border-color: var(--lav1); color: var(--text2); }
.det-result { background: linear-gradient(135deg, var(--pink4), var(--lav3)); border-radius: 12px; padding: 12px 14px; font-size: 12px; color: var(--text); margin-top: 10px; display: none; border: 1.5px solid var(--pink3); line-height: 1.7; }
.det-result.show { display: block; }
.det-result .rh { font-family: 'Gaegu', cursive; font-size: 15px; color: var(--pink1); margin-bottom: 5px; }
.det-poss { display: flex; flex-direction: column; gap: 5px; margin-top: 8px; }
.det-poss-item { display: flex; align-items: flex-start; gap: 7px; font-size: 12px; color: var(--text2); background: white; padding: 8px 11px; border-radius: 9px; border: 1.5px solid var(--border); }
.det-poss-num { font-family: 'Gaegu', cursive; font-size: 14px; color: var(--lav1); flex-shrink: 0; }
.det-next { margin-top: 10px; width: 100%; padding: 11px; background: linear-gradient(135deg, var(--pink1), var(--lav1)); border: none; border-radius: 12px; color: white; font-family: 'Gaegu', cursive; font-size: 15px; cursor: pointer; }

/* STORY */
.story-item { background: var(--pink4); border: 1.5px solid var(--pink3); border-radius: 12px; padding: 12px 14px; margin-bottom: 8px; position: relative; }
.story-item .si-q { font-size: 13px; font-weight: 700; color: var(--text); margin-bottom: 6px; }
.story-item .si-p { font-size: 12px; color: var(--text2); line-height: 1.7; }
.story-item .si-del { position: absolute; top: 9px; right: 10px; background: none; border: none; color: var(--muted); font-size: 14px; cursor: pointer; }

/* EDIT FORM (in card) */
.edit-form { background: var(--pink4); border: 2px solid var(--pink3); border-radius: 14px; padding: 14px; margin-top: 10px; display: flex; flex-direction: column; gap: 0; }
.edit-form .fl { font-size: 11px; color: var(--text2); font-weight: 900; text-transform: uppercase; letter-spacing: .8px; margin-bottom: 4px; display: block; }
.edit-form .fi { width: 100%; padding: 9px 12px; background: white; border: 1.5px solid var(--pink3); border-radius: 9px; color: var(--text); font-family: 'Noto Sans KR', sans-serif; font-size: 13px; outline: none; margin-bottom: 8px; resize: none; }
.edit-form .fi:focus { border-color: var(--pink1); }
.edit-form textarea.fi { line-height: 1.7; font-family: 'Noto Sans KR', sans-serif; }

/* SCROLLBAR */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--pink4); }
::-webkit-scrollbar-thumb { background: var(--pink2); border-radius: 4px; }

.section-label { font-size: 11px; font-weight: 900; color: var(--pink1); text-transform: uppercase; letter-spacing: 1px; margin: 12px 0 6px; padding-bottom: 4px; border-bottom: 2px solid var(--pink3); }

/* DET SCENE (in modal) */
.det-scene { background: linear-gradient(135deg, var(--lav3), var(--pink4)); border: 2px solid var(--lav2); border-radius: 16px; padding: 14px; margin-bottom: 10px; }
.det-scene-title { font-family: 'Gaegu', cursive; font-size: 16px; color: var(--lav1); margin-bottom: 6px; }
.det-input-row { display: flex; gap: 6px; align-items: flex-start; margin-bottom: 7px; }
.det-num { width: 28px; height: 28px; border-radius: 50%; background: linear-gradient(135deg, var(--pink1), var(--lav1)); color: white; font-family: 'Gaegu', cursive; font-size: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 1px; }
.det-input { flex: 1; padding: 8px 12px; background: white; border: 2px solid var(--lav2); border-radius: 10px; color: var(--text); font-family: 'Noto Sans KR', sans-serif; font-size: 13px; outline: none; }
.det-input:focus { border-color: var(--lav1); }
.det-hint { font-size: 11px; color: var(--lav1); font-weight: 700; margin-top: 3px; padding: 5px 11px; background: var(--lav3); border-radius: 8px; border: 1.5px solid var(--lav2); }
.det-result { background: linear-gradient(135deg, var(--mint3), var(--pink4)); border: 2px solid var(--mint2); border-radius: 12px; padding: 12px; margin-top: 8px; display: none; }
.det-result.show { display: block; }
.det-result-title { font-family: 'Gaegu', cursive; font-size: 15px; color: var(--mint1); margin-bottom: 6px; }
.det-ans { display: flex; align-items: flex-start; gap: 6px; margin-bottom: 5px; font-size: 12px; color: var(--text); line-height: 1.7; }
.det-checkbtn { width: 100%; padding: 11px; background: linear-gradient(135deg, var(--lav1), var(--pink1)); border: none; border-radius: 12px; color: white; font-family: 'Gaegu', cursive; font-size: 16px; cursor: pointer; margin-top: 4px; box-shadow: 0 3px 10px var(--shadow); }
.det-log { margin-top: 10px; }
.det-log-item { background: white; border: 1.5px solid var(--border); border-radius: 10px; padding: 9px 12px; margin-bottom: 6px; }
.det-log-sit { font-size: 11px; font-weight: 900; color: var(--text2); margin-bottom: 3px; }
.det-log-ans { font-size: 12px; color: var(--text); line-height: 1.7; }
.det-log-star { font-size: 11px; color: var(--pink1); font-weight: 900; margin-top: 3px; }
.det-scene-sel { width: 100%; padding: 9px 12px; background: white; border: 2px solid var(--lav2); border-radius: 10px; font-family: 'Noto Sans KR', sans-serif; font-size: 13px; color: var(--text); outline: none; margin-bottom: 8px; cursor: pointer; }
.det-custom-input { width: 100%; padding: 9px 12px; background: white; border: 2px solid var(--lav2); border-radius: 10px; font-family: 'Noto Sans KR', sans-serif; font-size: 13px; color: var(--text); outline: none; margin-bottom: 8px; }
.det-custom-input:focus, .det-scene-sel:focus { border-color: var(--lav1); }

/* STRATEGY CARDS */
.strat-section-title { font-size: 12px; font-weight: 900; color: var(--pink1); text-transform: uppercase; letter-spacing: .8px; margin: 4px 0 8px; padding-bottom: 4px; border-bottom: 1.5px solid var(--pink3); }
.strat-card { border: 2px solid var(--pink3); border-radius: 14px; padding: 12px 14px; margin-bottom: 8px; background: white; position: relative; overflow: hidden; }
.strat-card::before { content: ''; position: absolute; top: 0; left: 0; bottom: 0; width: 5px; }
.strat-i::before { background: var(--i-col); }
.strat-e::before { background: var(--e-col); }
.strat-card-top { display: flex; align-items: center; gap: 5px; flex-wrap: wrap; margin-bottom: 5px; }
.strat-rank { font-size: 16px; }
.strat-name { font-weight: 900; font-size: 14px; color: var(--text); }
.strat-badge { font-size: 10px; padding: 2px 8px; border-radius: 20px; font-weight: 700; }
.badge-i { background: rgba(29,78,216,.15); color: var(--i-col); }
.badge-e { background: rgba(180,83,9,.15); color: var(--e-col); }
.badge-g { background: var(--pink4); color: var(--text2); }
.strat-reasons { font-size: 11px; color: var(--text2); margin-bottom: 5px; font-weight: 700; }
.strat-advice { font-size: 12px; color: var(--text); background: var(--pink4); padding: 8px 11px; border-radius: 9px; border: 1.5px solid var(--pink3); line-height: 1.6; }
.strat-tip { font-size: 11px; color: var(--muted); margin-top: 5px; font-weight: 700; }
.strat-done { font-size: 13px; color: var(--mint1); font-weight: 900; padding: 10px; text-align: center; }
.strat-deepen { background: var(--lav3); border: 1.5px solid var(--lav2); border-radius: 12px; padding: 11px 14px; margin-bottom: 6px; }
.strat-subsection { border-left: 4px solid var(--pink3); padding: 10px 13px; margin-bottom: 8px; background: white; border-radius: 0 10px 10px 0; }
.strat-sub-title { font-size: 12px; font-weight: 900; margin-bottom: 5px; }
.strat-sub-body { font-size: 11px; color: var(--text2); line-height: 1.8; }

/* CALENDAR */
.cal-nav { background: var(--pink4); border: 1.5px solid var(--pink3); border-radius: 8px; padding: 4px 10px; font-size: 13px; cursor: pointer; color: var(--text2); font-family: 'Noto Sans KR', sans-serif; font-weight: 700; }
.cal-nav:hover { background: var(--pink3); }
.cal-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 3px; }
.cal-dow { text-align: center; font-size: 10px; font-weight: 900; color: var(--muted); padding: 3px 0; text-transform: uppercase; }
.cal-day { aspect-ratio: 1; border-radius: 10px; display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; border: 1.5px solid transparent; transition: all .15s; position: relative; min-height: 38px; }
.cal-day:hover { background: var(--pink4); }
.cal-day.today    { border-color: var(--pink1) !important; background: var(--pink4); }
.cal-day.has-score{ background: var(--lav3); }
.cal-day.streak   { background: linear-gradient(135deg, var(--pink4), var(--lav3)); }
.cal-day.selected { border-color: var(--pink1); background: var(--pink3); }
.cal-dn { font-size: 11px; font-weight: 700; color: var(--text2); }
.cal-ds { font-size: 10px; font-weight: 900; color: var(--pink1); }
.cal-dot { width: 5px; height: 5px; border-radius: 50%; background: var(--pink1); margin-top: 1px; }
.cal-streak-badge { position: absolute; top: -3px; right: -3px; background: var(--pink1); color: white; font-size: 7px; font-weight: 900; border-radius: 10px; padding: 1px 4px; line-height: 1.4; }
.cal-empty { aspect-ratio: 1; min-height: 38px; }
.detail-row { display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid var(--border); font-size: 12px; }
.detail-row:last-child { border: none; }
.detail-del { background: none; border: none; color: var(--muted); font-size: 14px; cursor: pointer; padding: 2px 5px; border-radius: 6px; }
.detail-del:hover { background: var(--pink3); color: var(--pink1); }

/* STREAK */
.streak-banner { background: linear-gradient(135deg, var(--pink1), var(--lav1)); border-radius: 12px; padding: 10px 14px; margin-bottom: 10px; color: white; display: flex; align-items: center; gap: 9px; }
.streak-num { font-family: 'Gaegu', cursive; font-size: 28px; line-height: 1; }
.streak-text { font-size: 12px; line-height: 1.5; font-weight: 700; }

/* RELATION STATUS */
.rstat { display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 900; margin-top: 3px; }
.rstat-growing  { background: rgba(13,148,136,.15);  color: #065F52; border: 1.5px solid rgba(13,148,136,.5); }
.rstat-stable   { background: rgba(29,78,216,.12);   color: #1D3A8A; border: 1.5px solid rgba(29,78,216,.4); }
.rstat-drifting { background: rgba(180,83,9,.12);    color: #7A3800; border: 1.5px solid rgba(180,83,9,.4); }
.rstat-distant  { background: rgba(109,40,217,.10);  color: #4A1A90; border: 1.5px solid rgba(109,40,217,.3); }
.rstat-btn { padding: 8px 6px; border-radius: 12px; border: 2px solid var(--border); background: white; font-size: 11px; cursor: pointer; font-family: 'Noto Sans KR', sans-serif; transition: all .15s; display: flex; flex-direction: column; align-items: center; gap: 3px; flex: 1; min-width: 0; text-align: center; min-height: 54px; justify-content: center; }
.rstat-btn:hover { border-color: var(--pink2); background: var(--pink4); }
.rstat-btn.sel-growing  { background: rgba(13,148,136,.12);  border-color: var(--mint1);     color: #065F52; }
.rstat-btn.sel-stable   { background: rgba(29,78,216,.10);   border-color: var(--i-col);     color: #1D3A8A; }
.rstat-btn.sel-drifting { background: rgba(180,83,9,.10);    border-color: var(--e-col);     color: #7A3800; }
.rstat-btn.sel-distant  { background: rgba(109,40,217,.10);  border-color: var(--bridge-col);color: #4A1A90; }
.rstat-icon  { font-size: 18px; display: block; }
.rstat-label { font-size: 10px; font-weight: 900; text-align: center; line-height: 1.3; white-space: normal; word-break: keep-all; }
.rstat-desc  { display: none; }

/* TIMELINE */
.rel-timeline { background: var(--pink4); border-radius: 12px; padding: 11px 13px; border: 1.5px solid var(--pink3); }
.rel-timeline-title { font-size: 11px; font-weight: 900; color: var(--text2); margin-bottom: 8px; }
.rel-history-item { display: flex; align-items: flex-start; gap: 8px; padding: 5px 0; border-bottom: 1px solid var(--border); font-size: 12px; }
.rel-history-item:last-child { border: none; }
.rel-history-dot { width: 9px; height: 9px; border-radius: 50%; flex-shrink: 0; margin-top: 3px; }

/* MOBILE */
#mapCanvas, #netCanvas { width: 100% !important; height: auto !important; touch-action: pan-y pinch-zoom; }
.mbox { padding: 14px 14px 20px !important; }
.mtab { font-size: 10px !important; padding: 7px 3px !important; }
.rstat-btn { padding: 6px !important; }
.agrid { grid-template-columns: 1fr 1fr !important; }
.stat-grid { grid-template-columns: repeat(4, 1fr) !important; }
.chips { gap: 5px !important; }
.chip { font-size: 11px !important; padding: 5px 10px !important; }
.hud { flex-wrap: nowrap; }
.hb { padding: 8px 3px !important; }
.hl { font-size: 9px !important; letter-spacing: 0 !important; }
.hv { font-size: 20px !important; }
.lpill { font-size: 10px !important; padding: 3px 8px !important; }

/* QUICK EDIT BUTTONS */
.acard-actions { display: flex; gap: 5px; margin-top: 8px; flex-wrap: wrap; }
.quick-edit-btn { display: inline-flex; align-items: center; gap: 3px; padding: 6px 12px; border-radius: 20px; border: 2px solid var(--border); background: white; color: var(--text2); font-size: 11px; font-weight: 700; cursor: pointer; font-family: 'Noto Sans KR', sans-serif; transition: all .15s; white-space: nowrap; }
.quick-edit-btn:hover, .quick-edit-btn:active { background: var(--pink1); color: white; border-color: var(--pink1); }
.quick-edit-btn.rel { border-color: var(--lav2); color: var(--lav1); }
.quick-edit-btn.rel:hover, .quick-edit-btn.rel:active { background: var(--lav1); color: white; border-color: var(--lav1); }
.quick-edit-btn.score { border-color: var(--mint2); color: var(--mint1); }
.quick-edit-btn.score:hover, .quick-edit-btn.score:active { background: var(--mint1); color: white; border-color: var(--mint1); }

/* UNIVERSAL EDIT */
.univ-edit-overlay { display: none; position: fixed; inset: 0; background: rgba(40,10,60,.5); z-index: 300; align-items: flex-end; justify-content: center; padding: 0; }
.univ-edit-overlay.open { display: flex; }
.univ-edit-box { background: white; border-radius: 22px 22px 0 0; width: 100%; max-width: 540px; max-height: 93vh; overflow-y: auto; -webkit-overflow-scrolling: touch; padding: 14px 14px 40px; box-shadow: 0 -10px 40px rgba(150,40,120,.3); }
.univ-edit-handle { width: 44px; height: 5px; background: var(--pink3); border-radius: 5px; margin: 0 auto 14px; cursor: pointer; }
.univ-section { margin-bottom: 14px; padding-bottom: 14px; border-bottom: 1.5px solid var(--border); }
.univ-section:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.univ-section-title { font-size: 12px; font-weight: 900; color: var(--pink1); text-transform: uppercase; letter-spacing: .8px; margin-bottom: 10px; display: flex; align-items: center; gap: 5px; }
.score-slider-wrap { background: var(--pink4); border-radius: 10px; padding: 10px 12px; border: 1.5px solid var(--pink3); }

input[type=range] { -webkit-appearance: none; height: 7px; border-radius: 6px; background: var(--pink3); outline: none; padding: 0; border: none !important; box-shadow: none !important; font-size: inherit !important; }
input[type=range]::-webkit-slider-thumb { -webkit-appearance: none; width: 24px; height: 24px; border-radius: 50%; background: var(--pink1); cursor: pointer; box-shadow: 0 2px 8px rgba(214,63,130,.5); }

/* MOBILE FIXES */
* { -webkit-tap-highlight-color: transparent; }
input, select, textarea { font-size: 16px !important; }
.app { max-width: 100%; width: 100%; }
.qc { padding: 14px; }
.moverlay { padding: 0; align-items: flex-end; }
.mbox { max-height: 88vh; padding: 15px 13px 28px; border-radius: 20px 20px 0 0; width: 100%; }
.rstat-icon { font-size: 15px; display: block; }
.rstat-label { font-size: 10px; }
.chips { gap: 5px; flex-wrap: wrap; }
.chip { padding: 6px 11px; font-size: 11px; white-space: nowrap; }
.agrid { gap: 6px; display: grid; grid-template-columns: 1fr 1fr; }
.act { padding: 9px 6px; font-size: 11px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 700; }
.hb { min-width: 0; overflow: hidden; }
.bpath { flex-wrap: nowrap; overflow-x: auto; -webkit-overflow-scrolling: touch; padding-bottom: 4px; }
canvas { display: block; box-sizing: border-box; touch-action: none; }
.acard { cursor: pointer; }
.rel-fullscreen { display: none; position: fixed; inset: 0; background: white; z-index: 300; overflow-y: auto; padding: 16px; }
.rel-fullscreen.open { display: block; }
.rel-fs-header { display: flex; align-items: center; gap: 10px; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 2px solid var(--pink3); }
.rel-fs-back { background: var(--pink4); border: 2px solid var(--pink3); color: var(--pink1); border-radius: 12px; padding: 8px 15px; font-size: 13px; font-weight: 700; cursor: pointer; font-family: 'Noto Sans KR', sans-serif; }
.rel-fs-title { font-family: 'Gaegu', cursive; font-size: 21px; color: var(--text); }
.edit-section { background: white; border: 2px solid var(--border); border-radius: 14px; padding: 13px; margin-bottom: 10px; }
.edit-section-title { font-size: 11px; font-weight: 900; color: var(--pink1); text-transform: uppercase; letter-spacing: .8px; margin-bottom: 8px; padding-bottom: 5px; border-bottom: 1.5px solid var(--pink3); }
.efi { font-size: 14px !important; padding: 10px 13px; margin-bottom: 8px; }
.strat-row { flex-wrap: wrap; }
.map-toolbar { flex-wrap: wrap; gap: 4px; }
.view-toggle { flex-wrap: nowrap; overflow-x: auto; scrollbar-width: none; gap: 4px; }
.vtbtn { font-size: 11px; white-space: nowrap; flex-shrink: 0; padding: 7px 11px; }
@media (min-width: 420px) {
  .stat-grid { grid-template-columns: repeat(4, 1fr); }
  .agrid { grid-template-columns: 1fr 1fr 1fr; }
}
</style>
</head>'''
print(html)
