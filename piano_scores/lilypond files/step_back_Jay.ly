#(set-default-paper-size "a4")

\paper {
  two-sided = ##t
  inner-margin = 0.5\in
  outer-margin = 0.5\in
  binding-offset = 0.25\in
}

\header{
  title = "step back"
  subtitle = "accompanyin"
  composer = "Jay"
  arranger = "GS Simulation"
}


melody = \relative c'' {
  % B part
  r1 r r r r r 
  r4. d8 d c d e e4 g,4.
  g8 d' c b c4 e,8 b' c4 e,8 
  a4 g4. g8 a b
  b c4 c8 c b c d 
  d g,4 d'8 d c d e
  e f,4 e'8 e d cis d
  e4. d8 d2  

  r4. d8 d c d e e4 g,4.
  g8 d' c b c4 c8 d c d e4 
  e2 e8 e g
  g f4 f8 e d c d
  f e4 e8 d e g, e'
  d c4 c8 c b c a' 
  a4. g8 g4. g,8

  % C part
  d'8 d d c b c16 d8 g8. 
  d8 d d c b c16 d8 e8. 
  e8 e e d cis d16 e8 f8.
  e8 e e d c d16 d16~ d8. g,16

  d'8 d d c b c16 d8 g8. 
  d8 d d c b c16 d8 c'8 
  b8([ c16 a2. ]) a16 b
  % repeat 1
  c8 c,16 c8. e8 d c b8. c16~
  c1
  
  r1 r1 r1
  % repeat 2
  c'8 c,16 c8. e8 d c b8. c16~
  c1 r1 r1 r2 r4 r8. g16
  
  d'8 d d c b c16 d8 g8. 
  d8 d d c b c16 d8 c'8 
  b8([ c16 a2. ]) a16 b
  c8 c,16 c8. e8 d c b8. c16~
  c1 r1 r1 r1 r1

}

text = \lyricmode {
天 空 灰 得 像 哭 過
離 開 你 以 後 並 沒 有   更 自 由 
酸 酸 的 空 氣   嗅 出 我 們 的 距 離 
一 幕 錐 心 的 結 局   像 呼 吸 般 無 法 停 息     

抽 屜 泛 黃 的 日 記   榨 乾 了 回 憶 
那 笑 容   是 夏 季   妳 我 的 過 去 被 順 時 針 的 忘 記 
缺 氧 過 後 的 愛 情   粗 心 的 眼 淚 是 多 餘 

我 知 道 妳 我 都 沒 有 錯   只 是 忘 了 怎 麼 退 後 
信 誓 旦 旦 給 了 承 諾   卻 被 時 間 撲 了 空 

我 知 道 我 們 都 沒 有 錯   只 是 放 手 會 比 較 好 過 
最 美 的 愛 情   回 憶 裡 待 續 

% repeat 2
的 愛 情   回 憶 裡 待 續  

我 知 道 我 們 都 沒 有 錯   只 是 放 手 會 比 較 好 過   
最 美 的 愛 情   回 憶 裡 待 續   
}

upper = \relative c'' {
  \time 4/4
  <g d'>8
  <g d'>8
  <g d'>8
  <g c>8
  <g b>8
  <g c>8
  <g d'>8
  <b g'>8

  <g d'>8
  <g d'>8
  <g d'>8
  <g c>8
  <d b'>8
  <e c'>8
  d'8
  <c e>8

  << { \voiceOne 
  e8 e e d d d d c
  }
  \new Voice { \voiceTwo 
  a2 g }
  >> \oneVoice

  <c, e>8
  <c e>
  <c e>
  d
  <d a g>4 <d b g>

  c8 g c16 d e f d2
  c8 g c16 d e f d2

%  \bar ".|:"

  % B part
  \repeat volta 2 {
  <c e>8 g <c e>8 g <c e>8 g <c e>8 g
  <d' g> g, <d' g> g, <d' g> g, <d' g> g,
  <c e>8 g <c e>8 g <c e>8 g <c e>8 g
  <d' g> g, <d' g> g, <d' g> g, <d' g> g,
  <c g'>8 a <c g'>8 a <d g>8 g, <d' g>8 g,
  <b d> g <b d> g <c e> g c16 d e c
  <c d f>8 a <c d f> a <cis f> a <cis f> a
  <f a d e>4 <f a d> <f g b d>2

  <c' d e>8 g <c d e>8 g <c d e>8 g <c d e>8 g
  <d' g> g, <d' g> g, <d' g> g, <d' g> g,
  <c e>8 g <c e>8 g <c e>8 g <c e>8 g
  <d' g> g, <d' g> g, <d' g> g, <d' g> g,
  <c g'>8 a <c g'>8 a <d g>8 g, <d' g>8 g,
  <b d> g <b d> g <c e> g c16 d e c
  <c d f>8 a d16 e f g <f a>8 c <f d'> c
  <c g'>4 <c g'>8 d <b g'>2

  % C part
  <d e g>4 <d e g>8 c <d e g>8 c d16 c b c
  <d e g>4 <d e g>8 c <d e g>8 c d16 c b c
  <c f>2. e16 d cis d
  <a c f>2. b16 c d g
  <d e g>4 <d e g>8 c <d e g>8 c d16 c b c
  <c e g>4 <e g>8 c <e g>8 c <b d g>4
  e8 a, c e <a e'> a <c a'> a |
  }
  
  \alternative {
  { <f c a>4 <f c a> <d b a> <d b a>
    <g d'>8 <g d'> d'16 e d8 b c g' c,
    <g d'>8 <g d'> d'16 e d8 b c g' c,
    <g d'>8 <g d'> d'16 e d8 b c g' c,
    <c, f> a <c f> a <b d g>2 | }
  
  { <f' c a>4 <f c a> <d b a> <d b a>8 g % octave follow previous alternative b, not repeat's a
    <g d'>8 <g d'> <g d'> c b c16 <g d'>8 g'8.
    <g, d'>8 <g d'> <g d'> c b c16 <g d'>8 g'8.
    <e a,>8 <e a,>8 <e a,>8 d cis d16 <e a,>8 f8.
    <e g,>8 <e g,>8 <e g,>8 d cis d16 <d g,>16~ <d g,>8. g,16
    | }
  }

  <d e g>4 <d e g>8 c <d e g>8 c d16 c b c
  <c e g>4 <e g>8 c <e g>8 c <b d g>4
  e8 a, <a' c> e <a e'> a <c a'> a 
    
  <f c a>4 <f c a> <d b a> <d b a>
  <g d'>8 <g d'> d'16 e d8 b c g' c,
  <g d'>8 <g d'> d'16 e d8 b c g' c,
  <g d'>8 <g d'> d'16 e d8 b c g' c,
  <c f,>^"rit." g <c f,> g <d g a b d>4\arpeggio g8 f
  <e d c g>1\arpeggio\fermata 

}

lower = \relative c {
  \clef bass
  % A part
  c8 g' d' e d e <b g b,>4
  a,8 e' c' e g,, e' c' d
  f,,8 c' a'4 e,8 c' g' e'
  d,,8 a'~ a4 g,2
  <c' e>2 <c f gis>
  <c e>2 <c f gis>

  % B part
  c,1
  e4~ e8~ e16 b e2
  a4.~ a16 e a2
  e4~ e8~ e16 b' e,2
  f4~ f8~ f16 c' f,2
  e4~ e8~ e16 e a2
  d,4.~ d16 d16 d4.~ d16 d16
  a'4.~ a16 d,16 g2

  c,1
  e4~ e8~ e16 b e2
  a4.~ a16 e a2
  e4~ e8~ e16 b' e,2
  f4~ f8~ f16 c' f,2
  e4~ e8~ e16 e a2
  d,4.~ d16 d16 d4.~ d16 d16
  g2 <g g,>2

  % C part
  c,2. b4
  a2.  g4
  d4.~ d16 d16 d4. f16 fis
  % repeat 1
  g4.~ g16 g g2 

  c2. b4
  a2.  g4
  d4.~ d16 d16 d4. f16 fis
  % repeat 2
  g4.~ g16 g g2 

  c'1 a f g

  g4.~ g16 g g2 
  c8 g' d' g, e' g, d' g,
  a, e' b' e, c' e, b' e,
  d, a' d a f' a, d a
  g d' b' d, <a' g,> d, b' d,  

  c,2. b4
  a2.  g4
  d4.~ d16 d16 d4. f16 fis
  g4.~ g16 g g2 

  c'8 g' c g d' g, c g
  a, e' a e b' e, a e
  f, c' f c a' c, f c
  g d' g d g,4 g,
  c1

}


\score {
  <<
    \new Voice = "mel" { \melody}
    \new Lyrics \lyricsto mel \text
    \new PianoStaff \with { instrumentName = #"Piano" } <<
      \new Staff = "upper" \upper
      \new Staff = "lower" \lower
    >>
  >>
}
