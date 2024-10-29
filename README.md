# CS 222: Assignment 1 - Creating Generative Agents

**Course:** AI Agents and Simulations  
**Institution:** Stanford University, Fall 2024  
**Contact:** mlarreaf@stanford.edu 

---

## Overview

This project demonstrates a generative agent chatbot that simulates a human-like conversational experience by storing, retrieving, and synthesizing memories. Designed around the persona "Matthew Jacobs," this agent recalls experiences and responds meaningfully in both factual and reflective dialogues, utilizing a memory database tailored to capture diverse life events and values. The goal was to showcase AI's capability to engage in dynamic conversations based on contextual and relevant memories, resulting in interactions that feel both nuanced and personal.

### Final Product

The completed chatbot agent can:
- **Retrieve and utilize memories** in response to direct factual questions, e.g., details of "Matthew Jacobs’" professional history or personal challenges.
- **Respond to reflective prompts** with insight into his life values and experiences, drawing on memories that reveal his motivations and growth.
- **Maintain coherence and relevance** in responses by prioritizing memories based on recency, importance, and relevance scoring.

For each response, the agent retrieves and ranks relevant memories, enhancing the interaction with realistic backstories and layered answers. Responses and the retrieved memories were logged and saved in CSV and JSON files to illustrate how the agent prioritized and used memory data.

### Project Components

1. **Memory Retrieval Functions**:  
   Implemented scoring functions to rank memories based on:
   - **Recency**: More recent memories receive higher importance.
   - **Importance**: Pre-determined importance scores influence retrieval.
   - **Relevance**: Memories are matched contextually using cosine similarity, enhancing the focus on pertinent information.

2. **Dialogue Interaction Module**:  
   Developed functions for generating responses that blend Matthew Jacobs’ personality traits with his memory database. This module uses prompt templates to synthesize responses that integrate his stored memories, including self-descriptions and experience-based insights.

3. **Persona Development**:  
   Built and configured "Matthew Jacobs," a fictional agent persona with a comprehensive memory set covering professional and personal milestones. This setup allowed for rich, character-driven responses, giving the agent a backstory that informs his conversational approach.

4. **Logging and Analysis**:  
   Saved interactions and top memory retrievals in CSV and JSON files, showing which memories were chosen per question and analyzing retrieval accuracy. A reflective report was created to assess retrieval effectiveness and the importance of memory relevance.

---

## Reflection and Analysis

The reflection explored memory retrieval efficiency, examining cases where memories accurately matched the conversational context versus instances where retrieval could be optimized. Through this analysis, distinctions emerged in how certain memories gain significance based on their emotional or narrative weight, which the agent learns to prioritize.

