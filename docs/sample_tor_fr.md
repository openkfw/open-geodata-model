# Termes de référence pour la collecte et la gestion des données de sites du projet dans le cadre du rapportage du projet

## 1.	Exigences communes : 

Les données relatives aux sites du projet feront partie des rapports réguliers sur la mise en œuvre du projet FC actuel (*insérer le titre du projet, l'abréviation du nom du projet (acronyme du projet), le numéro INPRO à 5 chiffres du projet KfW, la date de début (prévue) du projet officielle et le budget total du projet officiel*)  et seront jointes en annexe à chacun d'eux : rapport de planification (*si nécessaire*) et rapport (annuel / semestriel *- veuillez sélectionner !*) , rapport d'avancement, en commençant par le rapport de lancement du projet et se terminant par le rapport final. Par conséquent, les données relatives aux sites des projets doivent être **collectées, gérées et la qualité doit être garantie** par les parties qui sont responsables de la communication des rapports sur les projets en général et être distribuées aux mêmes parties qui reçoivent les rapports sur les projets, c'est-à-dire à toutes les parties prenantes concernées. Elles doivent être **mises à jour** au moins avec la même fréquence et la même qualité que les autres informations de déclaration (y compris le contenu minimal requis de l'en-tête et du pied de page de l'annexe), avec les exigences supplémentaires suivantes : 

- En plus d'être présentées en annexe à la version Word ou pdf du rapport, les données des sites du projet fournies doivent être soumises en parallèle dans le **modèle Excel de géodonnées du projet (et les fichiers KML respectifs pour les lignes et les polygones)** fournis dans le cadre du mandat pour la mise en œuvre du projet aux parties respectives du projet pour un traitement ultérieur des données sur le site web [Github](https://github.com/openkfw/open-geodata-model)

- Toutes les informations communiquées qui sont liées aux sites du projet, y compris les photos, les vidéos, les images satellites et les cartes, doivent indiquer **l'identifiant existant du lieu spécifique du projet** (c.-à-d. le numéro d'identification du lieu du projet, p. ex. 0001) dans la base de données des EPE/consultants. Si de tels identifiants n'existent pas encore, des identifiants uniques seront attribués aux sites dans les modèles mentionnés ci-dessus fournis par KfW après la soumission initiale du premier ensemble de données/fichier Excel.

## 2.	Exigences supplémentaires en matière de données: 

- Le modèle fourni (Excel et éventuellement KML) nécessite la fourniture de données standard sur les projets conformément aux exigences communes (chapitre 2) des exigences générales en matière de rapports KfW (voir également 1. Exigences communes). 

- En outre, les champs de données spécifiques aux sites doivent être remplis selon le modèle [Github](https://github.com/openkfw/open-geodata-model). Veuillez saisir le numéro de projet KfW à 5 chiffres ci-dessus dans le champ de données « numéro de projet » du modèle.

- Tous les sites de projets prévus ou existants et leurs attributs respectifs sont insérés dans le modèle ligne par ligne. Une ligne équivaut à un site de projet. Dans le cas où il n’est pas évident de définir les sites du projet (par exemple, dans certains cas, il est logique de résumer un certain nombre de petits projets dans une communauté sous un site de projet, dans d’autres cas, ce n’est pas le cas), cela doit être clarifié avec les parties bénéficiaires des rapports de projet. 

- La ou les classifications d'objet du CAD 5, également appelées code(s) CSR du projet, sont les suivantes : (@KfW : veuillez insérer tous les codes CSR attribués à votre projet dans la base de données interne - il s'agit d'un à quatre codes à 5 chiffres chaqun).  
Chaque site doit recevoir au moins un code CRS (obligatoire). Si plusieurs codes sont affectés à un même site, créez une ligne supplémentaire pour chaque code supplémentaire contenant les mêmes coordonnées GPS. Pour plus de détails, veuillez consulter [Github](https://github.com/openkfw/open-geodata-model).

- Les champs de données suivants indiqués comme non obligatoires dans le modèle Excel doivent être remplis pour ce projet (les cases ci-dessous doivent être cochées par la KfW) : 
- [ ] identifiant unique (seulement si ce modèle est une mise à jour. Pour les nouveaux modèles, ce champ de données restera vide, car KfW générera un ID unique pour chaque site dans son système
- [ ] Abréviation du nom du projet (acronyme du projet)
- [ ] Date de collecte des données ou dernière mise à jour
- [ ] Identifiant du site spécifique au projet (voir aussi ci-dessous)
- [ ] Statut de l’activité du site
- [ ] Description supplémentaire de l’activité
- [ ] Part du budget (somme totale de tous les sites = budget du projet officiel indiqué ci-dessus) en Euros
- [ ] Nom de Collectivité / Commune / Village / Quartier concerné
 
-	Pour chaque site de projet, il devrait y avoir un ensemble de données de géolocalisation exact ou approximatif, qui doit être mis à jour dans les intervalles de rapport réguliers susmentionnés. Les détails sont expliqués dans le modèle de localisation du projet de la KfW sur [Github](https://github.com/openkfw/open-geodata-model)

-	La fréquence des rapports et des changements de données de localisation est conforme aux exigences générales de rapport de la KfW (chapitre 6.1 : Progrès des services et des travaux) - annuellement ou deux fois par an ou autre, selon le type de projet (changement fréquent ou non des données de localisation, voir aussi le chapitre 1). 

-	Si un système d'information géographique (SIG), un système d'information de gestion (SIG) (à distance) ou un système de gestion de la maintenance (veuillez choisir lequel !)  est utilisé dans le projet, les identifiants de sites existants peuvent également être entrés dans le modèle Excel en tant qu'identificateurs d'emplacement spécifiques au projet (colonne G dans le tableau « Fill-Me / Remplis-moi » du modèle Excel de données de sites du projet. Il est ainsi plus facile de vérifier les données des sites dans les systèmes des partenaires du projet et l'utilisation des fonds.

## 3.	Cohérence des données
-	Il incombe au promoteur du projet/consultant chargé de la mise en œuvre du projet (veuillez choisir lequel !)  d'assurer la saisie de données normalisées (par exemple, des données de localisation correctes pour les lignes ou les points en utilisant la syntaxe précise).
-	Les champs de données, colonnes et/ou formules du modèle Excel ne sont pas modifiés. Des informations supplémentaires ne peuvent être fournies qu'en utilisant des colonnes supplémentaires à la fin du tableau (à droite). 
-	Il est de la responsabilité du promoteur du projet / du consultant en mise en œuvre du projet (veuillez choisir lequel !)  de fournir soit un fichier Excel entièrement fonctionnel (et dans le cas de lignes ou de polygones) un fichier KML supplémentaire selon le modèle joint avec tous les champs de données requis et des formules entièrement fonctionnelles. 

## 4.	Sécurité et confidentialité des données
-	Les consultants basés en Europe ou les promoteurs des projets / partenaires de mise en œuvre ou les consultants travaillant directement pour KfW sont légalement tenus de garantir la conformité de la collecte de données, y compris les sites web et les logiciels, à la fois avec les réglementations nationales pertinentes du pays dans lequel les données sont collectées ainsi qu'avec le règlement général sur la protection des données (RGPD, en Allemagne appelé DSGVO), tous les autres fournisseurs de données sont tenus de respecter les réglementations nationales pertinentes du pays dans lequel les données sont collectées.
-	Les données ne sont transférées que par des canaux cryptés (par exemple, la « data room » de la KfW). 
-	Une prudence particulière s'impose dans les contextes fragiles et conflictuels, où les données de sites ne doivent être traitées qu'avec une diligence particulière, par exemple en ne travaillant qu'avec des coordonnées géographiques approximatives pour des raisons de sécurité. 

Le modèle de localisaton du projet de la KfW fait partie de ces termes de référence y compris le modèle Excel ainsi que les icônes de type de sites en cours de mise à jour et les deux se trouvent ici sur [Github](https://github.com/openkfw/open-geodata-model). 
