"""Generate original GitHub profile artwork; no external image services."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import html

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'animated_assets'
OUT.mkdir(exist_ok=True)
FONT = Path('C:/Windows/Fonts')
def font(size, bold=False):
    return ImageFont.truetype(str(FONT / ('segoeuib.ttf' if bold else 'segoeui.ttf')), size)

W,H=1200,420
frames=[]
for i in range(64):
    t=i/64
    im=Image.new('RGB',(W,H),'#0b1220'); d=ImageDraw.Draw(im)
    for x in range(0,W,40): d.line((x,0,x,H),fill='#101d2e')
    for y in range(0,H,40): d.line((0,y,W,y),fill='#101d2e')
    d.rounded_rectangle((1,1,W-2,H-2),radius=24,outline='#25394d',width=2)
    d.rounded_rectangle((44,40,303,75),radius=16,fill='#133b3a')
    d.ellipse((58,52,68,62), fill='#59e3bb')
    d.text((80,45),'DATA  /  INSIGHT  /  ACTION',font=font(16,True),fill='#80e8d2')
    d.text((44,98),'ASAD ULLAH',font=font(68,True),fill='#f0f6fc')
    d.text((48,190),'Data Analyst & Power BI Developer',font=font(27),fill='#a8c4da')
    d.text((48,239),'Clear dashboards. Reliable metrics.',font=font(27,True),fill='#57dbc5')
    d.text((48,278),'Better business decisions.',font=font(27,True),fill='#57dbc5')
    d.line((48,340,602,340),fill='#25394d',width=2)
    d.text((48,359),'POWER BI     /     SQL     /     PYTHON',font=font(18,True),fill='#e1bb70')
    # Decorative analytics illustration: deliberately no performance claims.
    d.rounded_rectangle((708,56,1154,363),radius=22,fill='#101e30',outline='#2a4157',width=2)
    d.ellipse((730,77,739,86),fill='#57dbc5')
    d.text((751,70),'FROM DATA TO CLARITY',font=font(17,True),fill='#b2c9da')
    for y in (145,185,225,265): d.line((744,y,1119,y), fill='#223449')
    vals=[54,86,68,113,139,121,165,153]
    points=[]
    for j,v in enumerate(vals):
        x=751+j*50
        height=v+7*math.sin(2*math.pi*t+j*.55)
        d.rounded_rectangle((x,280-height,x+24,280),radius=5,fill='#1c5963' if j<6 else '#2c8f91')
        points.append((x+12,262-height))
    d.line(points,fill='#67efd0',width=4)
    # A softly moving point traces the trend.
    pos=t*7; k=min(int(pos),6); f=pos-k
    px=points[k][0]*(1-f)+points[k+1][0]*f
    py=points[k][1]*(1-f)+points[k+1][1]*f
    d.ellipse((px-8,py-8,px+8,py+8),fill='#214e50')
    d.ellipse((px-4,py-4,px+4,py+4),fill='#e1bb70')
    labels=['CLEAN','MODEL','EXPLAIN']
    for j,label in enumerate(labels):
        x=741+j*132
        d.rounded_rectangle((x,307,x+115,339),radius=8,fill='#173447')
        d.text((x+14,313),label,font=font(14,True),fill='#b8dce6')
    frames.append(im)
frames[0].save(OUT/'hero.gif',save_all=True,append_images=frames[1:],duration=90,loop=0,optimize=True)
frames[16].save(OUT/'hero_preview.png')

def svg(name,w,h,body):
    (OUT/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>',encoding='utf-8')

for name,label,color in [('portfolio','VIEW PORTFOLIO','#57dbc5'),('linkedin','CONNECT ON LINKEDIN','#83bfff')]:
    svg(name+'.svg',230,48,f'<rect x="1" y="1" width="228" height="46" rx="11" fill="#101e30" stroke="{color}"/><text x="115" y="29" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="700" fill="{color}">{label} &#8599;</text>')

body='<rect width="1200" height="90" rx="16" fill="#101e30"/>'
tools=['Power BI','DAX','Power Query','SQL','Python','Pandas','FastAPI']
for j,label in enumerate(tools):
    x=18+j*169
    body+=f'<rect x="{x}" y="20" width="150" height="50" rx="10" fill="#182d40" stroke="#2a4559"/><text x="{x+75}" y="51" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="18" font-weight="600" fill="{["#e1bb70","#7fe3cf","#a8c9e5"][j%3]}">{html.escape(label)}</text>'
svg('toolkit.svg',1200,90,body)
print('Created:',[(p.name,p.stat().st_size) for p in OUT.iterdir()])
