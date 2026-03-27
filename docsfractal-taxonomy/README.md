# Fractal Taxonomy

This folder contains notes and artifacts related to **fractal taxonomy**.

## What fractal taxonomy means

Fractal taxonomy is a way of structuring classification so that the **same organizing logic can repeat across levels** without having to be reinvented each time the scale changes.

In an ordinary taxonomy, you often get a fixed hierarchy:

- category
- subcategory
- sub-subcategory

That can work for filing and navigation, but it often becomes brittle as systems expand, concepts evolve, and AI begins interacting with material across multiple layers at once.

A fractal taxonomy is different.

It is not just a bigger hierarchy. It is a **recursive classification model** in which the same core logic can apply whether the object being classified is:

- an enterprise capability
- a department function
- a workflow
- a document
- a section
- a task
- a decision artifact

The scale changes, but the governing structure does not need to collapse or be redesigned.

## Why this matters

Fractal taxonomy matters because AI systems do not only need content. They need **stable classification logic**.

If classification changes arbitrarily from one level to another, then several problems appear quickly:

- retrieval becomes inconsistent
- inheritance becomes weak or confusing
- governance becomes harder to apply
- related objects stop being legible across levels
- machine interpretation becomes noisy
- future concepts become harder to integrate cleanly

A fractal taxonomy is meant to reduce that fragility by making the system more recursive, more extensible, and more interpretable.

## Core idea

The central claim of fractal taxonomy is:

**the same classification primitives should be able to recur across levels of the system.**

That does not mean every node is identical.  
It means every node can be understood through a familiar pattern.

For example, many nodes may still be describable through recurring fields such as:

- identity
- type
- parent
- child
- role
- status
- lifecycle
- related entities
- governing rules
- inheritance behavior

This makes the structure more stable over time and more useful for both humans and machines.

## Fractal taxonomy vs. ordinary taxonomy

### Ordinary taxonomy
Ordinary taxonomy is usually:
- linear
- static
- top-down
- brittle under growth
- useful for filing, but weaker for system intelligence

### Fractal taxonomy
Fractal taxonomy is:
- recursive
- reusable across levels
- more adaptable under growth
- better suited for inheritance and machine interpretation
- stronger as a foundation for ontology and decision systems

## Relationship to ontology

Taxonomy and ontology are not the same.

Taxonomy helps answer:
- What is this?
- What kind of thing is it?
- Where does it belong?
- What level is it at?

Ontology helps answer:
- What is it connected to?
- What depends on it?
- What does it constrain or enable?
- What meaning does it carry in context?

Fractal taxonomy is therefore not the entire system.  
It is one foundational layer.

Without stable taxonomy, ontology becomes harder to maintain because the underlying objects are not consistently classified.

## Relationship to decision-making

Fractal taxonomy also supports decision-making.

A decision system works better when the object in question is already legible:

- what type of thing is this?
- what category of governance applies?
- what lifecycle should it follow?
- what kind of review does it require?
- what escalation logic might be attached to it?

That means taxonomy is not only about organization. It is also part of how a system becomes **decision-ready**.

## Design principles

The approach in this node assumes several design principles:

### 1. Same logic, different scale
The same classification logic should be able to hold at multiple levels.

### 2. Stable primitives
A small number of recurring field families is better than endless local exceptions.

### 3. Extensibility
New concepts should be absorbed into the structure without requiring complete redesign.

### 4. Inheritance with control
Some properties should be able to flow downward or recur across nodes, while still allowing meaningful local overrides.

### 5. Human-readable and machine-readable alignment
The classification system should be understandable to people while remaining structured enough for AI and machine processes.

## What this folder is for

This folder is the dedicated node for developing the taxonomy side of the broader architecture.

It is where the repository can build out:

- recursive classification logic
- stable field families
- node types
- inheritance rules
- category and subcategory design
- lifecycle-aware classification
- metadata design for machine-readable artifacts
- taxonomy as a foundation for ontology and decision architecture

## Expected contents

Over time, this node may include:

- taxonomy definitions
- classification schemas
- field family models
- inheritance logic
- recursive node design
- category architecture notes
- examples across multiple levels
- machine-readable metadata
- crosswalks to ontology and decision-making

## Working thesis

Fractal taxonomy is not just a better filing system.

It is a way of creating a classification layer that can remain stable across levels, support future growth, and serve as a durable foundation for ontology, governance, and decision-making in AI-assisted systems.
