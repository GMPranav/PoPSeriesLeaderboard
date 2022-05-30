# PoP Series Leaderboard
A leaderboard/ranking system for Prince of Persia series speedruns. The way it works is by giving points to runners for every single run they have ever done (including obsoleted). The WR run of a category will get points equal to the number of verified runs in the category (including obsoleted), next best run will get that minus 1 point, and so on. Total points a runner gets is ofcourse the sum of all the points they accumulate across categories. Note that IL runs are not included.									

You can find the Leaderboard as of 30th May, 2022 here:
https://docs.google.com/spreadsheets/d/110hfO0Bkzj87bEX6_CFZmptytWzcKLpi0aIL_vt7T0E/view

## How to Use
* Run [Data.py](https://github.com/GMPranav/PoPSeriesLeaderboard/blob/main/Data.py), it will take a while to collect the run data and store in a file called "test.numpy".
* Download [Leaderboard.xlsx](https://github.com/GMPranav/PoPSeriesLeaderboard/blob/main/Leaderboard.xlsx), this is a template file that will be filled with points data.
* Run [RunSortC.py](https://github.com/GMPranav/PoPSeriesLeaderboard/blob/main/RunSortC.py) and it will fill Leaderboard.xlsx. Make sure to have test.numpy, RunSortC.py and Leaderboard.xlsx files in the same folder.

## For the curious

This whole thing works by collecting data from [speedrun.com's REST API](https://github.com/speedruncomorg/api). Every game, every run, every category and every sub-category have unique IDs, and it possible to sort out the runs after collecting it. I will list all of the PoP series IDs here:

### Games
```
Prince of Persia					yd4y2wde
Prince of Persia (Mods)					j1ll33j1
Prince of Persia (SNES) Romhacks		        o6gl4yxd
Prince of Persia (SNES)					76rxokq6
Prince of Persia 2: The Shadow and the Flame	        m1mq4xd2
Prince of Persia 3D					m1zqnx10
Prince of Persia Arabian Nights				3dx2v0y1
Prince of Persia: The Sands of Time (GBA)		v1pg4418
Prince of Persia: The Sands of Time			yd4r0g1e
Prince of Persia: Warrior Within			46wje7dr
Prince of Persia: The Two Thrones			v1ppz718
Battles of Prince of Persia				kdkzoz2d
Prince of Persia Classic				268k8y6p
Prince of Persia: The Fallen King			v1po7vz6
Prince of Persia 2008					76rykq18
Prince of Persia Mobile Games			        4d777rd7
Prince of Persia: The Forgotten Sands (PSP)		268qr96p
Prince of Persia: The Forgotten Sands (DS)		lde8ljd3
Prince of Persia: The Forgotten Sands (Wii)		j1nl5edp
Prince of Persia: The Forgotten Sands			j1l704dg
Multi-Prince of Persia-Runs                             369vv31l
```
### Categories
```
Prince of Persia:

  Any%	:	rklx8pnk {
    rqvvyeyq	:	DOS
    4qyxp34l	:	DOS (No Major Glitches)
    5le2xv6l	:	NES
    81w2ve51	:	Apple II
    81wm0j5q	:	TG-16
    zqo50dpl	:	GBC
    p12z2m41	:	SMS
    81pdo5v1	:	Amiga
    810y2o5l	:	Mega Drive
    klrv7woq	:	Genesis
  }

  Any% Level Skip	:	ndx9xq5d {
    klrnw4w1	:	DOS
    21dr7ggq	:	DOS (No Major Glitches)
  }

  100%	:	wkpq95gd{
    21ggx3m1	:	DOS
    jqz40mml	:	DOS (No Major Glitches)
  }

  Pacifist	:	mkeloznd

-----------------
Prince of Persia (Mods):

  Istaria	:	wdmvjyod

  Run, Prince! Run!	:	9kv8ww8d

-----------------
Prince of Persia (SNES):

  Any% (No Warp)	:	vdomz5y2

  Any%	:	8241l8m2

  Any% (No Gate Skip)	:	wkpm95gk

-----------------
Prince of Persia (SNES) Romhacks:

  Sunshine Remix	:	w20go3zk

  30th Anniversary Port	:	mkev0xx2

  The Queen of Light	:	5dw9l1n2

  Evolution	:	wdmxp4ek

  The Dark Castle	:	vdo8eo6k

-----------------
Prince of Persia 2 - The Shadow and the Flame:

  Any%	:	jdrpw3x2

-----------------
Prince of Persia 3D:

  Any%	:	jdz7lxvk

  Any% Alt-Tab	:	z27zlok0

-----------------
Prince of Persia - Arabian Nights:

  Any%	:	rklv09qd

-----------------
Prince of Persia - The Sands of Time:

  All Collectibles	:	zd3xnrdn{
    21d5m3le	:	Standard
    5q8pmrld	:	Zipless
    5leygm1o	:	No Major Glitches
  }

  Any%	:	xd1v9wd8{
    4qy963l7	:	Standard
    mln926qp	:	Zipless
    810prjlv	:	No Major Glitches

  }

  100%	:	zd3lmz8d{
    013w9krq	:	Standard
    rqv6v2rl	:	No Major Glitches
  }

-----------------
Prince of Persia - The Sands of Time (GBA):

  Any%	:	02q0gjky

-----------------
Prince of Persia - Warrior Within:

  Any%	:	02qnm92y{
    0q5mvvlp	:	Standard
    4lxk5g12	:	Zipless
    zqo7k51y	:	No Major Glitches
  }

  True Ending	:	wkp550dr{
    013ydrl5	:	Standard
    5lexv6qo	:	Zipless
    rqvngr16	:	No Major Glitches
  }

  All Collectibles	:	mke9qpjd{
  21gy9d61	:	No Major Glitches
  }

  All Chests	:	9kvoge82{
    jqzkge2q	:	Zipless
    xqk56vnq	:	No Major Glitches
  }

  All Artwork	:	wdmx13ok{
    jq63v07q	:	Standard
  }

-----------------
Prince of Persia - The Two Thrones:

  Any%	:	5dw11nkg{
    p12p0vqx	:	Standard
    81w2wm14	:	Zipless
    81p25el7	:	No Major Glitches
  }

  All Powers	:	n2yvvm2o{
    810y85lv	:	Standard
    9qjorgl4	:	Zipless
    rqvyeyq6	:	No Major Glitches
  }

  Any% PSP (US)	:	zd3xvzrd{
    81wwzv51	:	No Major Glitches
  }

-----------------
Prince of Persia Classic:

  Any%	:	9d8pn3wk

-----------------
Prince of Persia 2008:

  Any%	:	xd1rv6zk{
    jqzvpd4l	:	Standard
    gq793ndl	:	No Major Glitches
  }

  All Seeds	:	z276g30d

  Epilogue Any%	:	zd30xped

  Any% Hacked	:	zd366lyd

  Any% Dupe Glitch	:	xd170vwd

-----------------
Prince of Persia - The Fallen King:

  Any%	:	9kv74gjk{
    21go0xmq	:	Console
    gq7z37y1	:	Emulator
  }

-----------------
Prince of Persia - The Forgotten Sands:

  Any%	:	wdm4o54d{
    zqomxg51	:	Standard
    jqzxo941	:	No Energy Glitches
    013w9jrq	:	No Major Glitches
  }

-----------------
Prince of Persia - The Forgotten Sands (PSP):

  Any%	:	w201mqzk

-----------------
Prince of Persia - The Forgotten Sands (Wii):

  Any%	:	zd3l4vnd{
    xqkr6ey1	:	NG
    gq7nz5y1	:	NG+
  }

-----------------
Prince of Persia - The Forgotten Sands (DS):

  Any%	:	9kvj3q0k{
    81wr08ml	:	Console
    zqo2vn5l	:	Emulator
  }

-----------------
Prince of Persia Mobile Games:

  Harem Adventures	:	wk67pnxd

  Shadow and Flame (Remake)	:	mkerym6d

  Sands of Time	:	9kvmp78k

  Warrior Within	:	rklqxvn2

  The Two Thrones	:	ndxmj7r2

  Classic	:	vdoo0mvd

  2008	:	w20wpv5d

  The Forgotten Sands	:	wdmwzlo2

-----------------
Multi-Prince of Persia Games:

  Sands Trilogy	:	rklxvvqk
  {
    jq68rvlm	:	Any%
    {
      0q503m1p	:	Standard
      4lxj62q2	:	Zipless
      814nw0ld	:	No Major Glitches
    }
    81w6oml4	:	Completionist
    {
      0q503m1p	:	Standard
      4lxj62q2	:	Zipless
      814nw0ld	:	No Major Glitches
    }
  }

  Anthology	:	zdnrxgx2
```
