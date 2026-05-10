package com.example.dnd.ui

import com.example.dnd.network.DndApi

suspend fun generatePrompt(): String {
    val monsters = DndApi.service.getMonsters()
    val randomMonster = monsters.results.random()
    return "A ${randomMonster.name} in a dark, mysterious forest."
}