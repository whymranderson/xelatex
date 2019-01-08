#(set-default-paper-size "a4")

\paper {
  two-sided = ##f
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  #binding-offset = 0.25\in
}

\header{
  title = "Maple"
  subtitle = "accompanyin paino"
  composer = "Jay Chou"
  arranger = "Drillbits"
}


melody = \relative c'' {
\key c \major
r1 r r r r
r8 c8 c c c g c d
d  d  d8 e16 d16~d8 g,4.
r8 c8 c  c c d e f
f4. e8 e4. e8
d8 c16 c16 (c2) r8 e8
d c d e16 d16 (d8) c4.
c8 a16 c16 (c8) a16 c16 (c8) a16 c16 (c8) d8
d2. r4

r8 c8 c c c g c d
d  d  d8 e16 d16( d8) g,4.
r8 c8 c  c c d e f
f4 (f16) e16 d8 e4. e8
d8 c16 c16 (c2) r8 e8
d c d e16 d16 (d8) c4.
c8 a16 c16 (c8) a16 c16 (c8) a16 c16 (c8) a'8
g2. r4

r8 g,8 c b c d e c
d g4 g d8 c b
c c c b c d e f
(f) e4. r8 e8 e g
g a4 c,8 (c8) b b a'
a g g f16 f (f16) e8. r8 f16 g
g8 f f e16 e16 (e) d8. r8 d16 e
g8 f16 f16 (f16) e8. e8 d16 d (d) c8. 

r8 g8 c b c d e c
d g4 g d8 c b
c c c b c d e f
(f) e4. r8 e8 e g
g a4 c,8 (c8) b b a'
a g g f16 f (f16) e8. r8 f16 g
g8 f f e16 e16~e~d8. r8 d16 e
g8 f16 f16 (f16) e8. d8 c d8. c16
(c1) r1 r r

r8 c8 c c c g c d
d  d  d8 e16 d16( d8) g,4.
r8 c8 c  c c d e f
f4 (f16) e16 d8 e4. e8
d8 c16 c16 (c2) r8 e8
d c d e16 d16 (d8) c4.
c8 a16 c16 (c8) a16 c16 (c8) a16 c16 (c8) e8
d1

\key des \major
aes4. des8 des aes des ees
f4. ees16 bes (bes4.) ees8
ees8 des16 des16~ des8 c16 c16~c4. ees8
ees8 des des ees des4 c4
des4. aes'16 aes16~aes8 ges16 f8. ges8 
aes4. ges16 des~ des4. ees16 f16
ges8 f16 f ~f8 ees16 ees16~ ees4. ees16 f 
ges8 f16 f ~f16 ees8. ees8 des16 ees16~ees des8.

\repeat volta 2 {
r8 aes des c des ees f des
ees aes4 aes8~aes ees8 des c
des des des c des ees f ges~
ges f~f4. f8 f aes
aes bes4 des, c8 c bes' |
}

\alternative {
{bes aes aes ges16 ges16~ges16 f8. r8 ges16 aes
aes8 ges ges f16 f16~f16 ees8. r8 ees16 f
aes8 ges16 ges16~ges16 f8. f8 ees16 ees16~ees16 des8. |}
{bes'8 aes aes f16 c'16~c16 des8.~des4 |}
}

r2. r8 ges,16 aes
aes8 ges ges f16 f16~f16~ees8. r8 ees16 f
aes8 ges16 ges16~ges16 f8. ees8 des ees8. des16	~
des1
}

text = \lyricmode {
烏 雲 在 我 們 心 裡 擱 下 一 塊 陰 影 
我 聆 聽 沉 寂 已 久 的 心 情 
清 晰 透 明   就 像 美 麗 的 風 景   總 在 回 憶 裡 才 看 的 清 
被 傷 透 的 心 能 不 能 夠 繼 續 愛 我 
我 用 力 牽 起 沒 溫 度 的 雙 手 
過 往 溫 柔 已 經 被 時 間 上 鎖 
只 剩 揮 散 不 去 的 難 過 
緩 緩 飄 落 的 楓 葉 像 思 念 
我 點 燃 燭 火 溫 暖 歲 末 的 秋 天 
極 光 掠 奪 天 邊   北 風 掠 過 想 你 的 容 顏
我 把 愛 燒 成 了 落 葉   卻 換 不 回 熟 悉 的 那 張 臉 
緩 緩 飄 落 的 楓 葉 像 思 念 
為 何 挽 回 要 趕 在 冬 天 來 之 前 
愛 你 穿 越 時 間   兩 行 來 自 秋 末 的 眼 淚
讓 愛 滲 透 了 地 面   我 要 的 只 是 妳 在 我 身 邊 
被 傷 透 的 心 能 不 能 夠 繼 續 愛 我 
我 用 力 牽 起 沒 溫 度 的 雙 手 
過 往 溫 柔 已 經 被 時 間 上 鎖   只 剩 揮 散 不 去 的 難 過 
在 山 腰 間 飄 逸 的 紅 雨   隨 著 北 風 凋 零
我 輕 輕 搖 曳 風 鈴 
想   喚 醒 被 遺 棄 的 愛 情   雪 花 已 鋪 滿 了 地 
深 怕 窗 外 楓 葉 已 結 成 冰 

<<
{緩 緩 飄 落 的 楓 葉 像 思 念
我 點 燃 燭 火 溫 暖 歲 末 的 秋 天 
極 光 掠 奪 天 邊   北 風 掠 過 想 你 的 容 顏
我 把 愛 燒 成 了 落 葉   卻 換 不 回 熟 悉 的 那 張 臉 }

\new Lyrics 
\with { alignBelowContext = #"firstVerse" }
{
\set associatedVoice = "Voice"
緩 緩 飄 落 的 楓 葉 像 思 念 
為 何 挽 回 要 趕 在 冬 天 來 之 前
愛 你 穿 越 時 間   兩 行 來 {
\skip 1
}
}
>>
自 秋 末 的 眼 淚
讓 愛 滲 透 了 地 面   我 要 的 只 是 妳 在 我 身 邊 
}

upper = \relative c'' {
  \time 4/4
\key c \major

r2 c'8 e,16 b'16 (b16) c8. 
b8 d,16 g16 (g4) \acciaccatura g8 a8 c,16 g'16 (g16) f8. 
<c f>8 g16 e'16 d,8 d16 e c8 d16 e16( e16) c'8. 
b8 c c b16 c16 (c1)
r2

<g c d g>4 <g c g'>4 <g c g'>4 <g c g'>4
<g d' g> <g d' g> <g d' g> <g d' g> 
<a c f> <a c f> <a c f> <a c f> 
<g c f> <g c f> <g c e> <g c> 
<f c'> <f c'> <f a c> <f a c> 
<e g b> <e b'> <a c>8 e8 <a c e>4
<a, c f>4. <a c f>8 (<a c f>2)
<g' c d>4 <g c d>4 <g b d> r

<g c d g>4 <g c g'>4 <g c g'>4 <g c g'>4
<g d' g> <g d' g> <g d' g> <g d' g> 
<a c f> <a c f> <a c f> <a c f> 
<g c f> <g c f> <g c e> <g c> 
<f c'> <f c'> <f a c> <f a c> 
<e g c> <e g c> <c a' c>8 e8 <a c e>4
<a, c f>4. <a c f>8 (<a c f>2)
<c d g>4 <c d g>4 <b d g> <b d g>4

<c e>8 g <c e>8 g <c e>8 g <c e>8 g
<d' g> g, <d' g> g, <d' g> g, <gis' b>4
<a c>8 e <a c>8 e <a c>8 e <a c>8 e
<g b>8 e <g b>8 e <g b>8 e <g b>8 e 
<a c>8 f <a c>8 f <b d> g <b d> g
<g b>8 e <g b>8 e <a c>8 e <a c>8 e
<a d>8 f <a d>8 f <a d>8 f <a d>8 f
<g b>8 f <g b d>8 f <g b d>8 f <g b d>8 f

<c e>8 g <c e>8 g <c e>8 g <c e>8 g
<d' g> g, <d' g> g, <d' g> g, <gis' b>4
<a c>8 e <a c>8 e <a c>8 e <a c>8 e
<g b>8 e <g b>8 e <g b>8 e <g b>8 e 
<f a> c <f a> c <g' b> d <g b> d   
<e g> b <e g> b <e a> c <e a> c
<f a> d <f a> d <f a> d <f a> d
<g b> d <g b> d <gis b> d <gis b> d


r16 e c' b e, c' b e, c' b e, d' c b e, c'
e, c' b e, c' b e, c' b4 c32 b e, c b e, c b
c''16 e c' b e, c' b e, d' c b c b g d e
c d g8 c16  d g8 (g2)

<c,,, e>8 g <c e>8 g <c e>8 g <c e>8 g
<d' g> g, <d' g> g, <d' g> g, <d' g> g,
<c f> a <c f> a <c f> a <c f> a 
<c g'> g <c g'> g <c e> g <c e> g 
<c f> a <c f> a <c f> a c16 d e g
<e g>8 b <e g>8 b <e a> c <e a> c
<f, c'>4. <f c'>8 (<f c' >2)
<c' d g>2 <b d g>8 <g' c>8 <g d'>8 <g e'>8

\key des \major
<aes des>8 f <aes des>8 f <aes des>8 f <aes des>8 f
<bes des> ges <bes des> ges <bes des> ges <bes des> ges
<aes c> ges <aes c> ges <aes c> ges <aes c> ges
<ges bes> ees <ges bes> ees <aes c> ees <aes c> ees
<aes des> f <aes des> f <aes des> f <aes des> f
<bes des> ges <bes des> ges <bes des> ges <bes des> ges
<aes c> <f ges> <aes c> ges <aes c> ges <aes c> ges
<ges bes> ees <ges bes> ees <aes c> ees <aes c> ees

<des f> aes <des f> aes <des f> aes <des f> aes
<ees' aes> aes, <ees' aes> aes, <ees' aes> aes, <a' c> ees
<bes' des> f <bes des> f <bes des> f <bes des> f

<aes c> f <aes c> f <aes c> f <aes c> f
<ges bes> des <ges bes> des <aes' c> ees <aes c> ees
<f aes> c <f aes> c <f ges bes> des <f bes> des
<ees ges> bes <ees ges> bes <ees ges> bes <ees ges> bes
<ees aes> c <ees aes> c <ees ges aes> c <ees ges aes> c

<aes' c> f <aes c> f <g bes des>16 f bes des f bes des f
bes4 <f des' f> ees,, f4
<bes, ges'> <bes ges'> <bes ges'> <bes ges'> 
<des aes'> des c2
des4 des des des 
des1
}

lower = \relative c {
  \clef bass
\key c \major
r2 a8 e'8 c'4 
e,8 g d'4 f,,8 c'8 g'4 
c,4 <b g'> a r4
<e' g b>2 <f a>8 <c d>8 g'16 a c8 
<g, d' g c>2 <g' b>2


c1
b1
a1
g2. e4
f1
e2 <a c>
<d,, d'>4.  <d d'>8~<d d'>2 
g'2 g2

c,1
b
a1
g2. <e' d'>4
f,1
e2 a2
<d, d'>4.  <d d'>8~<d d'>2 
<g g'>4. d'8 <g, d'>2

c,4.~c16 c16 c4 r8 g16 a
b4. ~b16 b   b4    gis
a4. ~a16 e   a4.   c16 d
e4. ~e16 b   e4.   d16 e
f2           f4.   d16 f
e4. ~e16 e16 a,2
d,4. ~d16 d16 d4.  ~d16 d16
g4. ~g16 g16 g4    g4

c1
b2           gis
a4. ~a16 a16 a4.   c16 d
e4. ~e16 e16 e4.   d16 e
f4. ~f16 f16 f4.   d16 f
e4. ~e16 e16 a,2
d,4. ~d16 d16 d2
g2 gis

<a' e'>1
<f c'>
<a' e'>
<f, c'>

c'1
b1
a1
g2 g2
f1
e2 a2
<d, d'>4.  <d d'>8~ <d d'>2
<g g'>2 <g g'>2

\key des \major
des'1
ges1
aes1
ees2 aes
des1
ges,1
aes
ees2 aes

des,,2.~des8 aes16 bes 
c2. a'4
bes1
f2.~f8  des,16 ees
f2.~f8  ees'16 ges
f2 bes,
ees1
aes,1
f'2 g2~
g1
ees'1
<aes, aes'>4 aes' <aes, ges'>2
<des, des'>8 f' aes f aes f aes f
des,,1
}

violin = \relative c{
c e'' g, c,
b, b'' g d8 e8
<g g'>2 c'8 g <e d'>4
<c f a>4 c'8 g c4 <c, f a>4
<e g b>2 <a, a'>
<f d' f>4 r8 <f d' f>8 <f d' f>2 
<g d'>4 (<g d'>8) g'8 <g, d'>4 <g d'>4
}

\score {
  <<
    \new Voice = "mel" { \melody}
    \new Lyrics = "firstVerse" \lyricsto mel \text
    \new PianoStaff \with { instrumentName = #"Piano" } <<
      \new Staff = "upper" \upper
      \new Staff = "lower" \lower
    >>
  >>  
  \layout { }
  \midi { }
 }

