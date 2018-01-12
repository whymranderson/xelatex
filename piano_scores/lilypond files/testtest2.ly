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


}
%}
\header{
  title = "Marry me today"
  subtitle = "Accompanying piano score"
  composer = "Tao Gee Gee"
  arranger = "GS Simulation"
}

fluteNotes = \relative c'' {
  r4 e, a cis 
  fis4. e8 e4 cis8 b
  cis2. r8 cis8 d 
  e fis4 e d8 cis b a2 r4.
  ees'4 d cis8 bes aes g~
  g2. r4  
  d'8 cis cis a b4 d4 c1
  \absolute { e''8 e''8 e''8 e''8 e''4 d''8 c''8 e''8 e''8 e''8 e''8 e''4. r8
  e''8 e''8 e''8 e''8 e''8 f''8 g''8 d''4 c''4. c''2
  c''8 c''8 c''8 c''8 c''8 d''8 c''8 g''4 e''8 g''8 d''4 c''4 r8 
  c''8 d''8 d''8 d''8 a'8 b'4 d''4 c''1  } }

violinNotes = \relative c'' {
  r1
  e2. f16 e d8 
  e2 r8 e f g 
  a4 g f8 e d
  c~ c1
  r1 r1 r1
  \quoteDuring #"flute" { s1 }
  \chordmode {c1  }%c:7^5.7/b}
  <b, e g>
  <bes e g>
  <a c f>
  <aes c f>
  <g c e >
  <f  a  d>2
  <g  b  d>2
  \chordmode {c1}
}

\addQuote "flute" { \fluteNotes }

\score {
  <<
    \new Staff \with { instrumentName = "Flute" } \fluteNotes
    \new Staff \with { instrumentName = "Violin" } \violinNotes
  >>
}
