### Project: AI in Connect4
iets over het project :3

#### Begin:

**Het bevat de klasse Board uit opgave 2 van week 10:**

Voor de Board class hebben wij onze eigen variant gebruikt, deze hebben we wel nagekeken met het voorbeeld in de opdracht.


**Het bevat een klasse Player met een werkende constructor en __repr__:**  
Voor de constructor en representation method hebben we de code gekopieerd uit de opdracht. Heb alleen variable namen verandert naar iets wat duidelijkere namen.  
`ox` -> `char`  
`tbt` -> `tie_breaking_type`  
`ply` -> `turns`   
Dit is hetzelfde in de class Board om consistentie te behouden.


**Deze klasse bevat twee werkende methodes opp_ch en score_board:**  
`opp_ch()` was aardig makkelijk te implementeren omdat hetzelfde idee in opdracht wk11ex2 wordt gebruikt. We vroegen ons wel af of we er van uit moesten gaan dat het character (ox) altijd X of O is. Voor nu gegaan voor een if-elif-condition waar we heel specifiek op de X en O checken en anders niks returnen, wou eerst een Exception maken maar uiteindelijk weer weggehaald.

`score_board(board)` was ook zo klaar, eerst checken of jij zelf wint (self.char). Als hij heeft gewonnen volgens `Board.wins_for(char)` `100.0` punten terug sturen. Zo niet, dan checken of tegenstander (`self.opp_ch()`) wint. wint hij dat stuur
je `0.0` points terug. Anders heeft self.char niet gewonnen, maar ook niet verloren en kan je `50.0` punten terug sturen.

**Github:**  
Om dit project samen te maken, maken we gebruik van Github. We gooien alle requirements gesplit in issues en lossen deze op in onze eigen 'development' branches, na goedkeuring worden ze samengevoegd met de master/main branche.
