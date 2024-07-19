document.addEventListener('DOMContentLoaded', function() {
    const brChallenge = document.querySelector('.br-challenge');
    const nbrChallenge = document.querySelector('.nbr-challenge');
    const damageAmountBR = brChallenge.querySelector('.damage-amount-br');
    const damageCategoryBR = brChallenge.querySelector('.damage-category-br');
    const damageAmountNBR = nbrChallenge.querySelector('.damage-amount-nbr');
    const selectedWeaponTextNBR = nbrChallenge.querySelector('.selected-weapon-text-nbr');
    const selectedWeaponBR = nbrChallenge.querySelector('.selected-weapon-br');

    // Initialisation avec les valeurs par défaut de BR
    updateDamageAmountBR();
    selectedWeaponBR.textContent = damageCategoryBR.value; // Mettre à jour le texte de l'arme sélectionnée pour NBR avec l'arme sélectionnée de BR

    // Écouter les changements dans la sélection d'arme BR
    damageCategoryBR.addEventListener('change', function() {
        updateDamageAmountBR();
        selectedWeaponBR.textContent = damageCategoryBR.value; // Mettre à jour la sélection d'arme affichée dans NBR
    });

    // Fonction pour mettre à jour la quantité de dommage BR
    function updateDamageAmountBR() {
        const selectedOptionBR = damageCategoryBR.options[damageCategoryBR.selectedIndex];
        const damageAmountBRValue = parseInt(selectedOptionBR.getAttribute('data-damage-amount'));
        damageAmountBR.textContent = damageAmountBRValue;

        // Définir les dégâts fixes pour chaque arme dans NBR
        const damageValuesNBR = {
            "Assault Rifles": 15000,
            "Light Machine Guns": 10000,
            "Marksman Weapons": 5000,
            "Pistols": 2500,
            "Shotguns": 3500,
            "Sniper Rifles": 5000,
            "Sub Machine Guns": 15000,
        };

        const selectedWeaponValueBR = selectedOptionBR.value;
        const fixedDamageNBR = damageValuesNBR[selectedWeaponValueBR];
        damageAmountNBR.textContent = fixedDamageNBR;

        selectedWeaponTextNBR.textContent = selectedWeaponValueBR; // Mettre à jour le texte de l'arme sélectionnée dans NBR
    }
});
