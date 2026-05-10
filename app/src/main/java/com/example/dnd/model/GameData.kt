package com.example.dnd.model

data class Race(
    val name: String,
    val abilityBonuses: Map<String, Int>,
    val speed: Int,
    val size: String,
    val languages: List<String>,
    val traits: List<String>
)

data class Class(
    val name: String,
    val hitDie: Int,
    val primaryAbility: String,
    val savingThrows: List<String>,
    val skillsCount: Int,
    val skillsAvailable: List<String>,
    val startingEquipment: List<String>,
    val proficiencies: List<String>
)

data class Background(
    val name: String,
    val skillProficiencies: List<String>,
    val toolProficiencies: List<String>,
    val equipment: List<String>,
    val feature: String
)

data class Character(
    val name: String,
    val race: Race,
    val characterClass: Class,
    val background: Background,
    val abilityScores: Map<String, Int>,
    val skills: List<String>,
    val inventory: List<String>
)