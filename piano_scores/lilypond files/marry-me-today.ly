%{
Welcome to LilyPond
===================

Congratulations, LilyPond has been installed successfully.

Now to take it for the first test run.

  1. Save this LilyPond file on your desktop with the name "test.ly".

  2. Pick it up from the desktop with your mouse pointer, drag and drop
     it onto the LilyPond icon.

  3. LilyPond automatically produces a PDF file from the musical scale
     below.

  4. To print or view the result, click on the newly produced file
     called

        test.pdf

  5. If you see a piece of music with a scale, LilyPond is working properly.

Next, you'll want to get started on your own scores.  To do this you'll 
  need to learn about using LilyPond.

LilyPond's interface is text-based, rather than graphical. Please visit the
  help page at http://lilypond.org/introduction.html.  This will
  point you to a quick tutorial and extensive documentation.

Good luck with LilyPond!  Happy engraving.



\version "2.16.0"  % necessary for upgrading to future LilyPond versions.

\header{
  title = ""
  subtitle = "For more information on using LilyPond, please see
http://lilypond.org/introduction.html"
}
%}

#(set-default-paper-size "letter")

\paper {
  two-sided = ##t
  inner-margin = 0.25\in
  outer-margin = 0.25\in
  binding-offset = 0.25\in
}

\header{
  title = "今天妳要嫁給我"
  subtitle = "樂器伴奏譜"
  composer = "陶喆"
  arranger = "GS Simulation"
}


fluteNotes = \relative c'' {
  r1
  e2~ e4 e8 d~ d 
  e2 e8 f g 
  a4 g f8 e d
  c~ c1
  
  ees4 d c8 bes aes g 
  e1
  d'8 c c a b4 d
  c1
  
  e8 e e e e4 d8 c
  e8 e e e e2
  e8 e e e e f g d4
  c2~ c4.
  c8 c c c c d c g'4
  e8 g d4 c
  c8 d d d e d c b d c1

  e8 e e e e4 d8 c
  e8 e e e e2
  e8 e e e e f g d4
  c2~ c4.
  c8 c c c c d c g'4
  e8 g d4 c
  c8 d d d e d c b d 
  c4. 
  
  g'8 a4 g
  g g g e8 f
  g4 g g e8 f 
  g4 g a g
  c,1
  f8 f f f g4 f
  e8 e e e f4 e
  d8 d d a b4 d
  c1
  
  
%{  r4 e, a cis 
  fis4. e8 e4 cis8 b
  cis2. r8 cis8 d 
  e fis4 e d8 cis b a2 r4.
  ees'4 d cis8 bes aes g~
  g2. r4  
  d'8 cis cis a b4 d4 c1
%}
}

violinNotes = \relative c'' {
 
  r4 g c e
  a4. g8 g2~
  g1
  a4 g2.
  c,1
  
  g'4 f2.
  r1
  r1
  r1
  
  c1 b bes a
  aes g f2 g2
  c1
  
  c1 b bes 
  a'4 g f c
  aes1 g f2 g2
  c1
  
  c'8 b b a a g c, d 
  e1
  r1
  a4 g f c
  aes1 g a2 b2
  c1
  
\quoteDuring #"flute" { s1 }
}

\addQuote "flute" { \fluteNotes }

words = \lyricmode {
}

pianoNotes = \relative c'' {

\set Score.skipBars = ##t
R1*9

c8 g d' d4 c4 g8 %e~ e2

b8 g d' d4 b g8 

bes8 g d' d4 bes g8


\acciaccatura { a,8} a'4 g f c

aes

\set Score.skipBars = ##t
R1*20


  r2. c8 d  
  e2~ e4 e8 d~ d 
  e2 e8 f g 
  a4 g f8 e d
  c~ c1
  
  ees4 d c8 bes aes g 
  e1
  d'8 c c a b4 d
  c1



\quoteDuring #"flute" { s1 }
}

\addQuote "flute" { \fluteNotes }

%up = \drummode {
%  r1 hh16 hh hh r8. hh16 hh r8 hh16 hh hh hh hh r16
%}
%down = \drummode {
%  r1 bassdrum4 snare8 bd r bd sn4
%}

drumNotes = \relative c'' {
r1 c16 c c r8. c16 c r8 c16 c c c c r16
}

bassNotes = \relative c'' {
r1 
a8 a4 e16 a8 a4.
d8 d4 a d d d e d

}


\score {
  <<
    \new Staff \with { instrumentName = "Vocal" } \fluteNotes
    \addlyrics \words
    \new Staff \with { instrumentName = "Violin" } \violinNotes
    \new Staff \with { instrumentName = "Piano/Guitar" } \pianoNotes
    \new RhythmicStaff \with { instrumentName = "drum" } \drumNotes
    \new Staff \with { instrumentName = "bass" } \bassNotes
%    \new DrumStaff \with { instrumentName = "drum/bass" } <<
%      \new DrumVoice { \voiceOne \up }
%      \new DrumVoice { \voiceTwo \down }
%>>
  >>
}
