package com.example.dnd.ui.character

import androidx.lifecycle.ViewModel
import com.example.dnd.model.Background
import com.example.dnd.model.Class
import com.example.dnd.model.Race

class CharacterCreatorViewModel : ViewModel() {
    // For simplicity, using placeholder data. 
    // In a real app, this would be loaded from the GameDataParser.
    val races = listOf(Race("Human", emptyMap(), 30, "Medium", emptyList(), emptyList()))
    val classes = listOf(Class("Fighter", 10, "Strength", emptyList(), 2, emptyList(), emptyList(), emptyList()))
    val backgrounds = listOf(Background("Soldier", emptyList(), emptyList(), emptyList(), ""))

    var selectedRace: Race? = null
    var selectedClass: Class? = null
    var selectedBackground: Background? = null
}