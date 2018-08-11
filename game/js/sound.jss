var EATING_SOUND = new buzz.sound([
    "./sound/eating.txt" 
]);
var GHOST_EATEN_SOUND = new buzz.sound([
	"./sound/ghost-eaten.txt" 
]);
var EXTRA_LIFE_SOUND = new buzz.sound([
    "./sound/extra-life.txt" 
]);
var EAT_PILL_SOUND = new buzz.sound([
    "./sound/eat-pill.txt" 
]);
var EAT_FRUIT_SOUND = new buzz.sound([
    "./sound/eat-fruit.txt" 
]);
var EAT_GHOST_SOUND = new buzz.sound([
    "./sound/eat-ghost.txt" 
]);
var SIREN_SOUND = new buzz.sound([
    "./sound/siren.txt" 
]);
var WAZA_SOUND = new buzz.sound([
    "./sound/waza.txt" 
]);
var READY_SOUND = new buzz.sound([
    "./sound/ready.txt" 
]);
var DIE_SOUND = new buzz.sound([
    "./sound/die.txt" 
]);

var GROUP_SOUND = new buzz.group([ EATING_SOUND, SIREN_SOUND, EAT_PILL_SOUND, EAT_GHOST_SOUND, READY_SOUND, DIE_SOUND, WAZA_SOUND, GHOST_EATEN_SOUND, EXTRA_LIFE_SOUND, EAT_FRUIT_SOUND ]);

var EATING_SOUND_LOOPING = false;

function isAvailableSound() { 
	return !($("#sound").css("display") === "none");
}

function loadAllSound() { 
	if ( isAvailableSound() ) GROUP_SOUND.load();
}

function playEatingSound() { 
	if (isAvailableSound()) { 
		if ( !EATING_SOUND_LOOPING ) { 
			EATING_SOUND_LOOPING = true;
			
			EATING_SOUND.setSpeed(1.35);
			EATING_SOUND.loop();
			EATING_SOUND.play();
		}
	}
}
function stopEatingSound() { 
	if (isAvailableSound()) { 
		if ( EATING_SOUND_LOOPING ) { 
			EATING_SOUND.unloop();
			EATING_SOUND_LOOPING = false;
		}
	}
}

function playExtraLifeSound() { 
	if (isAvailableSound()) { 
		EXTRA_LIFE_SOUND.play();
	}
}

function playEatFruitSound() { 
	if (isAvailableSound()) { 
		EAT_FRUIT_SOUND.play();
	}
}
function playEatPillSound() { 
	if (isAvailableSound()) { 
		EAT_PILL_SOUND.play();
	}
}
function playEatGhostSound() { 
	if (isAvailableSound()) { 
		EAT_GHOST_SOUND.play();
	}
}

function playWazaSound() { 
	if (isAvailableSound()) { 
		stopSirenSound();
		stopEatSound();
		WAZA_SOUND.loop();
		WAZA_SOUND.play();
	}
}
function stopWazaSound() { 
	if (isAvailableSound()) { 
		WAZA_SOUND.stop();
	}
}

function playGhostEatenSound() { 
	if (isAvailableSound()) { 
		stopSirenSound();
		stopWazaSound();
		GHOST_EATEN_SOUND.play();
		GHOST_EATEN_SOUND.loop();
	}
}
function stopEatSound() { 
	if (isAvailableSound()) { 
		GHOST_EATEN_SOUND.stop();
	}
}

function playSirenSound() { 
	if (isAvailableSound()) { 
		stopWazaSound();
		stopEatSound();
		SIREN_SOUND.loop();
		SIREN_SOUND.play();
	}
}
function stopSirenSound() { 
	if (isAvailableSound()) { 
		SIREN_SOUND.stop();
	}
}

function playReadySound() { 
	if (isAvailableSound()) { 
		READY_SOUND.play();
	}
}

function playDieSound() { 
	if (isAvailableSound()) { 
		GROUP_SOUND.stop();
		DIE_SOUND.play();
	}
}

function stopAllSound() { 
	if (isAvailableSound()) { 
		GROUP_SOUND.stop();
	}
}