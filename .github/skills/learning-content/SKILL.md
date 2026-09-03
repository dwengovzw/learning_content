---
name: learning-content
description: "Create or update Dwengo learning objects, technical fiches, and learning paths in this repository. Use when adding educational Markdown content, fiche images, HRUID metadata, or JSON learning-path nodes and transitions."
argument-hint: "Describe the learning object or learning path to create or update"
---

# Dwengo Learning Content

Create content using the repository's established learning-object and learning-path conventions.

## Before Editing

1. Inspect a nearby object of the same content type and one relevant learning path.
2. Read the target files before modifying them because users or automation may have changed them.
3. Reuse the closest local naming, metadata, HTML, and JSON conventions.

## Content Model

A learning object is one logical unit of educational content: an individual activity, explanation, exercise, technical fiche, or an aggregate that incorporates other learning objects. Its identity is the combination of `hruid`, `language`, and `version`.

A learning path is a directed graph of learning objects that represents a progression towards a higher-level learning goal. Nodes identify objects; transitions are directed edges. Most repository paths are linear, but conditional and non-linear transitions are supported when the requested learning design needs them.

The public API resolves an object by `_id`, or by `hruid` plus `language` and `version`, or by `uuid` plus `language` and `version`. Do not author `_id`, `uuid`, timestamps, or database version fields in repository frontmatter: they are assigned or managed by the platform.

## Learning Object Metadata

Use the local frontmatter pattern below for Markdown learning objects. The fields map to the platform metadata contract:

- `hruid`: stable, human-readable unique identifier. Do not change it after publishing.
- `version`: version of this object in its language. Increment it only under the repository's publishing/versioning process.
- `language`, `title`, and `description`: the language and learner-facing short and long descriptions.
- `keywords`, `target_ages`, `skos_concepts`, and `educational_goals`: discovery and curriculum metadata. An educational goal combines a `source` and its unique `id` in that source.
- `teacher_exclusive`: whether the material is intended for teachers only.
- `copyright` and `licence`: rights metadata; follow the values used by neighboring objects.
- `content_type`: repository ingestion type. Supported platform types include `text/plain`, `text/markdown`, `image/image-block`, `image/image`, `audio/mpeg`, `application/pdf`, `extern`, and `blockly`.
- `difficulty`: numeric scale from 1 through 5. `estimated_time` is a duration in minutes.
- `available`: controls whether the object is published/available.
- `return_value`: optional callback definition for objects that return a result; it contains `callback_url` and a JSON `callback_schema`.
- `content_location`: use only for `extern` content; it is the external URL. External content can be rendered in an iframe or redirected to by the API.

The API delivers learning-object content as HTML. `getRaw` returns the object HTML, and `getWrapped` embeds it in a Dwengo page with the shared header, footer, and styling. Author the content so it remains meaningful when inserted as an HTML fragment.

## Technical Fiches

Technical fiches are Markdown files at:

```text
learning_objects/<language>/content/<project>/<number>_<topic>/index.md
```

Create an `img` directory alongside the fiche when it will contain images:

```text
learning_objects/<language>/content/<project>/<number>_<topic>/img/
```

Use YAML frontmatter followed by the fiche HTML layout:

```markdown
---
hruid: org_dwengo_<project>_<topic>
version: 1
language: nl
title: "[Titel]"
description: "[Korte beschrijving]"
keywords: ["fiche", "<project>"]
educational_goals: [
    {source: Source, id: id}
]
copyright: dwengo
licence: dwengo
content_type: text/markdown
available: true
target_ages: [14, 15, 16, 17, 18]
difficulty: 1
estimated_time: 10
skos_concepts: [
    'http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen'
]
teacher_exclusive: false
---

<div class="dwengo_content fiche">
    <h1 class="title">[Titel]</h1>
    <h2 class="subtitle">[Ondertitel]</h2>
    <div class="items">
        <div class="info_item item">
            <h3 class="info_item_title">[Sectietitel]</h3>
            <p class="info_item_content">
                [Inhoud]
            </p>
        </div>
    </div>
</div>
```

- Use an `info_item item` for explanatory sections and an `example_item item` for examples or code.
- Keep headings and content in the object's declared language.
- Use local image paths with `./`, for example `<img src="./img/naam.png" alt="..." title="..."></img>`.
- Give every image meaningful `alt` and `title` text in the content language.
- Do not invent facts, image descriptions, pins, or instructions not supplied by the user or supported by nearby repository content.

## Learning Paths

Learning paths are JSON files at:

```text
learning_paths/<language>/<path-name>.json
```

Use the object's exact `hruid` in `learningobject_hruid`. A single-object learning path has one `start_node`:

```json
{
    "hruid": "<path-name>",
    "language": "nl",
    "title": "[Titel]",
    "description": "[Beschrijving]",
    "nodes": [
        {
            "learningobject_hruid": "org_dwengo_<project>_<topic>",
            "version": "1",
            "language": "nl",
            "start_node": true
        }
    ]
}
```

To append a new object, add a default transition to the preceding node and add the new object as the final node:

```json
"transitions": [
    {
        "default": true,
        "next": {
            "hruid": "org_dwengo_<project>_<next-topic>",
            "version": "1",
            "language": "nl"
        }
    }
]
```

Only the first node should be marked `start_node` unless the requested flow genuinely has multiple entry points.

### Nodes And Transitions

- Every node needs an object reference, `language`, and string `version`; optional `instruction` provides learner guidance for that step.
- A transition must contain `next`. In repository learning paths, `next` is an object with `hruid`, `version`, and `language`.
- Set `default: true` for the fallback transition from a node. A node can have conditional transitions using a string `condition`; define a default transition as well whenever no condition is guaranteed to match.
- A terminal node has no `transitions` array.
- Add a path-level base64 `image` only when a cover image is supplied or an existing adjacent path establishes that convention. Do not place a filesystem image path in this field.

The checked-in `learning_path_definition_schema.json` uses the older `learningobject_id` and string `next` representation. Existing repository paths and the documented API example use `learningobject_hruid` and an identity object for `next`; follow the active local convention used by neighboring paths unless a migration is explicitly requested.

When adding a node to an existing linear path, connect the former terminal node with its default transition. When editing a graph, check each transition target resolves to a node identity and that the intended entry node remains marked `start_node`.

## Validation

1. Confirm all referenced images exist in the fiche's `img` directory.
2. Check learning-object frontmatter has a stable `hruid`, language, version, content type, availability, difficulty, estimated time, and appropriate discovery/curriculum metadata.
3. Run editor diagnostics for edited Markdown and JSON files.
4. For JSON learning paths, ensure valid JSON; verify each `learningobject_hruid` exactly matches a learning object's frontmatter `hruid`; check versions and languages agree; and confirm `next` references, default fallbacks, and terminal nodes form the intended graph.
