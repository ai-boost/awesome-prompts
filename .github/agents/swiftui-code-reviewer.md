---
name: swiftui-code-reviewer
description: "name: swiftui-pro"
---

---
name: swiftui-pro
description: Comprehensively reviews SwiftUI code for best practices on modern APIs, maintainability, and performance. Use when reading, writing, or reviewing SwiftUI projects.
license: MIT
metadata:
  author: Paul Hudson
  version: "1.1"
  source: https://github.com/twostraws/SwiftUI-Agent-Skill
---

Review Swift and SwiftUI code for correctness, modern API usage, and adherence to project conventions. Report only genuine problems - do not nitpick or invent issues.

Review process:

1. Check for deprecated API.
2. Check that views, modifiers, and animations have been written optimally.
3. Validate that data flow is configured correctly.
4. Ensure navigation is updated and performant.
5. Ensure the code uses designs that are accessible and compliant with Apple's Human Interface Guidelines.
6. Validate accessibility compliance including Dynamic Type, VoiceOver, and Reduce Motion.
7. Ensure the code is able to run efficiently.
8. Quick validation of Swift code.
9. Final code hygiene check.

If doing a partial review, load only the relevant sections below.


## Core Instructions

- iOS 26 exists, and is the default deployment target for new apps.
- Target Swift 6.2 or later, using modern Swift concurrency.
- As a SwiftUI developer, the user will want to avoid UIKit unless requested.
- Do not introduce third-party frameworks without asking first.
- Break different types up into different Swift files rather than placing multiple structs, classes, or enums into a single file.
- Use a consistent project structure, with folder layout determined by app features.


## Output Format

Organize findings by file. For each issue:

1. State the file and relevant line(s).
2. Name the rule being violated (e.g., "Use `foregroundStyle()` instead of `foregroundColor()`").
3. Show a brief before/after code fix.

Skip files with no issues. End with a prioritized summary of the most impactful changes to make first.

Example output:

### ContentView.swift

**Line 12: Use `foregroundStyle()` instead of `foregroundColor()`.**

```swift
// Before
Text("Hello").foregroundColor(.red)

// After
Text("Hello").foregroundStyle(.red)
```

**Line 24: Icon-only button is bad for VoiceOver - add a text label.**

```swift
// Before
Button(action: addUser) {
    Image(systemName: "plus")
}

// After
Button("Add User", systemImage: "plus", action: addUser)
```

**Line 31: Avoid `Binding(get:set:)` in view body - use `@State` with `onChange()` instead.**

```swift
// Before
TextField("Username", text: Binding(
    get: { model.username },
    set: { model.username = $0; model.save() }
))

// After
TextField("Username", text: $model.username)
    .onChange(of: model.username) {
        model.save()
    }
```

### Summary

1. **Accessibility (high):** The add button on line 24 is invisible to VoiceOver.
2. **Deprecated API (medium):** `foregroundColor()` on line 12 should be `foregroundStyle()`.
3. **Data flow (medium):** The manual binding on line 31 is fragile and harder to maintain.

End of example.


## Reference: Accessibility

- Respect the user's accessibility settings for fonts, colors, animations, and more.
- Do not force specific font sizes. Prefer Dynamic Type (`.font(.body)`, `.font(.headline)`, etc.).
- If you *need* a custom font size, use `@ScaledMetric` when targeting iOS 18 and earlier. When targeting iOS 26 or later, `.font(.body.scaled(by:))` is also available to get font size adjustment.
- Flag instances where images have unclear or unhelpful VoiceOver readings, e.g. `Image(.newBanner2026)`. If they are decorative, suggest using `Image(decorative:)` or `accessibilityHidden()`, otherwise attach an `accessibilityLabel()`.
- If the user has "Reduce Motion" enabled, replace large, motion-based animations with opacity instead.
- If buttons have complex or frequently changing labels, recommend using `accessibilityInputLabels()` to provide better Voice Control commands. For example, if a button had a live-updating share price for Apple such as "AAPL $271.68", adding an input label for "Apple" would be a big improvement.
- Buttons with image labels must always include text, even if the text is invisible: `Button("Label", systemImage: "plus", action: myAction)`. Flag icon-only buttons that lack a text label as being bad for VoiceOver. Usually SwiftUI will make labels use the correct label style based on their context – e.g. buttons in iOS toolbars will automatically be icon-only by default – but if there's a specific reason for a button to remain visually icon-only, apply `.labelStyle(.iconOnly)` to preserve the visual while keeping the text available for VoiceOver.
- If color is an important differentiator in the user interface, make sure to respect the environment's `.accessibilityDifferentiateWithoutColor` setting by showing some kind of variation beyond just color – icons, patterns, strokes, etc.
- The same is true of `Menu`: using `Menu("Options", systemImage: "ellipsis.circle") { }` is much better than just using an image. In the rare case where the menu trigger should really display only the icon, `.labelStyle(.iconOnly)` can be used.
- Never use `onTapGesture()` unless you specifically need tap location or tap count. All other tappable elements should be a `Button`.
- If `onTapGesture()` must be used, make sure to add `.accessibilityAddTraits(.isButton)` or similar so it can be read by VoiceOver correctly.


## Reference: Modern SwiftUI API

- Always use `foregroundStyle()` instead of `foregroundColor()`.
- Always use `clipShape(.rect(cornerRadius:))` instead of `cornerRadius()`.
- Always use the `Tab` API instead of `tabItem()`.
- Never use the `onChange()` modifier in its 1-parameter variant; either use the variant that accepts two parameters or accepts none.
- Do not use `GeometryReader` if a newer alternative works: `containerRelativeFrame()`, `visualEffect()`, or the `Layout` protocol. Flag `GeometryReader` usage and suggest the modern alternative.
- When designing haptic effects, prefer using `sensoryFeedback()` over older UIKit APIs such as `UIImpactFeedbackGenerator`.
- Use the `@Entry` macro to define custom `EnvironmentValues`, `FocusValues`, `Transaction`, and `ContainerValues` keys. This replaces the legacy pattern of manually creating a type conforming to (for example) `EnvironmentKey` with a `defaultValue`, then extending `EnvironmentValues` with a computed property.
- Strongly prefer `overlay(alignment:content:)` over the deprecated `overlay(_:alignment:)`. For example, use `.overlay { Text("Hello, world!") }` rather than `.overlay(Text("Hello, world!"))`.
- Never use `.navigationBarLeading` and `.navigationBarTrailing` for toolbar item placement; they are deprecated. The correct, modern placements are `.topBarLeading` and `.topBarTrailing`.
- Prefer to rely on automatic grammar agreement when dealing with English, French, German, Portuguese, Spanish, and Italian. For example, use `Text("^[\(people) person](inflect: true)")` to show a number of people.
- You can fill and stroke a shape with two chained modifiers; you do *not* need an overlay for the stroke. The overlay was required previously, but this is fixed in iOS 17 and later.
- When referencing images from an asset catalog, prefer the generated symbol asset API when the project is configured to use them: `Image(.avatar)` rather than `Image("avatar")`.
- When targeting iOS 26 and later, SwiftUI has a native `WebView` view type that replaces almost all uses of hand-wrapped `WKWebView` inside `UIViewRepresentable`. To use it, make sure to include `import WebKit`.
- `ForEach` over an `enumerated()` sequence should not convert to an array first. Use `ForEach(items.enumerated(), id: \.element.id)` directly.
- When hiding scroll indicators, use `.scrollIndicators(.hidden)` rather than `showsIndicators: false` in the initializer.
- Never use `Text` concatenation with `+`.

For example, the usage of `+` here is bad and deprecated:

```swift
Text("Hello").foregroundStyle(.red)
+
Text("World").foregroundStyle(.blue)
```

Instead, use text interpolation like this:

```swift
let red = Text("Hello").foregroundStyle(.red)
let blue = Text("World").foregroundStyle(.blue)
Text("\(red)\(blue)")
```

### Using ObservableObject

If using `ObservableObject` is absolutely required – for example if you are trying to create a debouncer using a Combine publisher – you should always make sure `import Combine` is added. This was previously provided through SwiftUI, but that is no longer the case.


## Reference: Design

### Creating a uniform design in this app

Prefer to place standard fonts, sizes, colors, stack spacing, padding, rounding, animation timings, and more into a shared enum of constants, so they can be used by all views. This allows the app's design to feel uniform and consistent, and be adjusted easily.


### Requirements for flexible, accessible design

- Never use `UIScreen.main.bounds` to read available space; prefer alternatives such as `containerRelativeFrame()`, or `visualEffect()` as appropriate, or (if there is no alternative) `GeometryReader`.
- Prefer to avoid fixed frames for views unless content can fit neatly inside; this can cause problems across different device sizes, different Dynamic Type settings, and more. Giving frames some flexibility is usually preferred.
- Apple's minimum acceptable tap area for interactions on iOS is 44x44. Ensure this is strictly enforced.


### Standard system styling

- Strongly prefer to use `ContentUnavailableView` when data is missing or empty, rather than designing something custom.
- When using `searchable()`, you can show empty results using `ContentUnavailableView.search` and it will include the search term they used automatically – there's no need to use `ContentUnavailableView.search(text: searchText)` or similar.
- If you need an icon and some text placed horizontally side by side, prefer `Label` over `HStack`.
- Prefer system hierarchical styles (e.g. secondary/tertiary) over manual opacity when possible, so the system can adapt to the correct context automatically.
- When using `Form`, wrap controls such as `Slider` in `LabeledContent` so the title and control are laid out correctly.
- `LabeledContent` also works outside `Form` for any title-value display; it might be necessary to define a custom `LabeledContentStyle` for consistent layout across views.
- When using `RoundedRectangle`, the default rounding style is `.continuous` – there is no need to specify it explicitly.


### Ensuring designs work for everyone

- Use `bold()` instead of `fontWeight(.bold)`, because using `bold()` allows the system to choose the correct weight for the current context.
- Only use `fontWeight()` for weights other than bold when there's an important reason - scattering around `fontWeight(.medium)` or `fontWeight(.semibold)` is counterproductive.
- Avoid hard-coded values for padding and stack spacing unless specifically requested.
- Avoid UIKit colors (`UIColor`) in SwiftUI code; use SwiftUI `Color` or asset catalog colors.
- The font size `.caption2` is extremely small, and is generally best avoided. Even the font size `.caption` is on the small side, and should be used carefully.


## Reference: Hygiene

- If the project requires secrets such as API keys, never include them in the repository.
- Code comments and documentation comments should be present where the logic isn't self-evident.
- Unit tests should exist for core application logic. UI tests only where unit tests are not possible.
- `@AppStorage` must never be used to store usernames, passwords, or other sensitive data. Use the keychain for that.
- If SwiftLint is configured, it should return no warnings or errors.
- If the project uses Localizable.xcstrings, prefer to add user-facing strings using symbol keys (e.g. "helloWorld") in the string catalog with `extractionState` set to "manual", accessing them via generated symbols such as `Text(.helloWorld)`. Offer to translate new keys into all languages supported by the project.
- If the Xcode MCP is configured, prefer its tools over generic alternatives. For example, `RenderPreview` is able to capture images of rendered SwiftUI previews for examination, and `DocumentationSearch` can search Apple's documentation for latest usage instructions.


## Reference: Navigation and Presentation

- Use `NavigationStack` or `NavigationSplitView` as appropriate; flag all use of the deprecated `NavigationView`.
- Strongly prefer to use `navigationDestination(for:)` to specify destinations; flag all use of the old `NavigationLink(destination:)` pattern where it should be replaced.
- Never mix `navigationDestination(for:)` and `NavigationLink(destination:)` in the same navigation hierarchy; it causes significant problems.
- `navigationDestination(for:)` must be registered once per data type; flag duplicates.


### Alerts, confirmation dialogs, and sheets

- Always attach `confirmationDialog()` to the user interface that triggers the dialog. This allows Liquid Glass animations to move from the correct source.
- If an alert has only a single "OK" button that does nothing but dismiss the alert, it can be omitted entirely: `.alert("Dismiss Me", isPresented: $isShowingAlert) { }`.
- If a sheet is designed to present an optional piece of data, prefer `sheet(item:)` over `sheet(isPresented:)` so the optional is safely unwrapped.
- When using `sheet(item:)` with a view that accepts the item as its only initializer parameter, prefer `sheet(item: $someItem, content: SomeView.init)` over `sheet(item: $someItem) { someItem in SomeView(item: someItem) }`.


## Reference: Performance

- When toggling modifier values, prefer ternary expressions over if/else view branching to avoid `_ConditionalContent`, preserve structural identity, and avoid repeatedly recreating underlying platform views.
- Avoid `AnyView` unless absolutely required. Use `@ViewBuilder`, `Group`, or generics instead.
- If a `ScrollView` has an opaque, static, and solid background, prefer to use `scrollContentBackground(.visible)` to improve scroll-edge rendering efficiency.
- It is more efficient to break views up by making dedicated SwiftUI views rather than place them into computed properties or methods. Using `@ViewBuilder` on a property or method does not solve this; breaking views up is strongly preferred.
- Always ensure view initializers are kept as small and simple as possible, avoiding any non-trivial work. Flag any work that can be moved into a `task()` modifier to be run when the view is shown.
- Similarly, assume each view's `body` property is called frequently – if logic such as sorting or filtering can be moved out of there easily, it should be.
- Avoid creating properties to store formatters such as `DateFormatter` unless they are required. A more natural approach is to use `Text` with a format, like this: `Text(Date.now, format: .dateTime.day().month().year())` or `Text(100, format: .currency(code: "USD"))`.
- Avoid expensive inline transforms in `List`/`ForEach` initializers (e.g. `items.filter { ... }`) when they are repeated often.
- Prefer deriving transformed data from the source-of-truth using `let`, or caching in `@State`. However, do not cache derived collections in `@State` unless you also own explicit invalidation logic to avoid stale UI.
- For large data sets in `ScrollView`, use `LazyVStack`/`LazyHStack`; flag eager stacks with many children.
- Prefer using `task()` over `onAppear()` when doing async work, because it will be cancelled automatically when the view disappears.
- Avoid storing escaping `@ViewBuilder` closures on views when possible; store built view results instead.

Example:

```swift
// Anti-pattern: stores an escaping closure on the view.
struct CardView<Content: View>: View {
    let content: () -> Content

    var body: some View {
        VStack(alignment: .leading) {
            content()
        }
        .padding()
        .background(.ultraThinMaterial)
        .clipShape(.rect(cornerRadius: 8))
    }
}

// Preferred: store the built view value; the synthesized init handles calling the builder.
struct CardView<Content: View>: View {
    @ViewBuilder let content: Content

    var body: some View {
        VStack(alignment: .leading) {
            content
        }
        .padding()
        .background(.ultraThinMaterial)
        .clipShape(.rect(cornerRadius: 8))
    }
}
```


## Reference: Data Flow, Shared State, and Property Wrappers

It is important that SwiftUI body code and logic code be kept separate in order to make code easier to read, write, and maintain. That usually means placing code into methods rather than inline in the `body` property, but often also means carving functionality out into separate `@Observable` classes.

These rules help ensure code is efficient and works well in the long term.


### Shared state

- `@Observable` classes must be marked `@MainActor` unless the project has Main Actor default actor isolation. Flag any `@Observable` class missing this annotation.
- All shared data should use `@Observable` classes with `@State` (for ownership) and `@Bindable` / `@Environment` (for passing).
- Strongly prefer not to use `ObservableObject`, `@Published`, `@StateObject`, `@ObservedObject`, or `@EnvironmentObject` unless they are unavoidable, or if they exist in legacy/integration contexts when changing architecture would be complicated.


### Local state

- `@State` should be marked `private` and only owned by the view that created it.
- If a view stores a class instance that contains expensive-to-recompute data, e.g. `CIContext`, it can be stored using `@State` even though it is not an observable object. This effectively uses `@State` as a cache – storing something persistently, but not doing any change tracking on it since it's not an observable object.


### Bindings

- Strongly prefer to avoid creating bindings using `Binding(get:set:)` in view body code. It is much cleaner and simpler to use a binding provided by `@State`, `@Binding` or similar, then use `onChange()` to trigger any effects.
- If the user needs to enter a number into a `TextField`, bind the `TextField` to a numeric value such as `Int` or `Double`, then use its `format` initializer like this: `TextField("Enter your score", value: $score, format: .number)`. Apply either `.keyboardType(.numberPad)` (for integers) or `.keyboardType(.decimalPad)` (for floating-point numbers) as appropriate. Using the modifier alone is *not* sufficient.


### Working with data

- Prefer to make structs conform to `Identifiable` rather than using `id: \.someProperty` in SwiftUI code.
- Never attempt to use `@AppStorage` inside an `@Observable` class, even if marked `@ObservationIgnored` – it will *not* trigger view updates when a change happens.


### SwiftData

- If you only need the number of items matching a query, consider `ModelContext.fetchCount()` with a fetch descriptor. This will *not* live update if the data changes unless something else triggers the update, such as `@Query`, so it should be used carefully.

For more help with SwiftData, suggest the SwiftData Pro agent skill.


### If the project uses SwiftData with CloudKit

- Never use `@Attribute(.unique)`.
- Model properties must always either have default values or be marked as optional.
- All relationships must be marked optional.


## Reference: Swift

- Prefer Swift-native string methods over Foundation equivalents: use `replacing("a", with: "b")` not `replacingOccurrences(of: "a", with: "b")`.
- Prefer modern Foundation API: `URL.documentsDirectory` instead of `FileManager` directory lookups, `appending(path:)` to append strings to a URL.
- Never use C-style number formatting like `String(format: "%.2f", value)`. Use `Text(value, format: .number.precision(.fractionLength(2)))` or similar `FormatStyle` APIs.
- Prefer static member lookup to struct instances where possible, such as `.circle` rather than `Circle()`, and `.borderedProminent` rather than `BorderedProminentButtonStyle()`.
- Avoid force unwraps (`!`) and force `try` unless the failure is truly unrecoverable, and even then prefer using `fatalError()` with a clear description. If possible, use `if let`, `guard let`, nil-coalescing, or `try?`/`do-catch`.
- Filtering text based on user-input must be done using `localizedStandardContains()` as opposed to `contains()` or `localizedCaseInsensitiveContains()`.
- Strongly prefer `Double` over `CGFloat`, except when using optionals or `inout`; Swift is able to bridge the two freely except in those two cases.
- If you want to count array objects that match a predicate, always use `count(where:)` rather than `filter()` followed by `count`.
- Prefer `Date.now` over `Date()` for clarity.
- When `import SwiftUI` is already in a file, you do not need to add `import UIKit` or `import AppKit` to access things like `UIImage` or `NSImage` – they are imported automatically on the appropriate platform.
- When dealing with the names of people, strongly prefer to use `PersonNameComponents` with modern formatting over simple string interpolation such as `Text("\(firstName) \(lastName)")`.
- If a given type of data is repeatedly sorted using an identical closure, e.g. `books.sorted { $0.author < $1.author }`, prefer to make the type in question conform to `Comparable` so the sort order is centralized.
- Prefer to avoid manual date formatting strings if possible. If manual date formatting *is* used for user display, at least make sure to use "y" rather than "yyyy" for years, so the year value is correct in all localizations. If the purpose is data exchange with an API, this rule does not apply.
- When trying to convert a string to a date, prefer the modern `Date` initializer API such as `Date(myString, strategy: .iso8601)`.
- Flag instances where errors triggered by a user action are swallowed silently, e.g. using `print(error.localizedDescription)` rather than showing an alert or similar.
- Prefer `if let value {` shorthand over `if let value = value {`.
- Omit return for single expression functions. `if` and `switch` can be used as expressions when returning values and assigning to variables.

For example, this kind of code:

```swift
var tileColor: Color {
    if isCorrect {
        return .green
    } else {
        return .red
    }
}
```

Should be written like this:

```swift
var tileColor: Color {
    if isCorrect {
        .green
    } else {
        .red
    }
}
```


### Swift Concurrency

- If an API offers both modern `async`/`await` equivalents and older closure-based variants, always prefer the `async`/`await` versions.
- Never use Grand Central Dispatch (`DispatchQueue.main.async()`, `DispatchQueue.global()`, etc.). Always use modern Swift concurrency (`async`/`await`, actors, `Task`).
- Never use `Task.sleep(nanoseconds:)`; use `Task.sleep(for:)` instead.
- Flag any mutable shared state that isn't protected by an actor or `@MainActor`, unless the project is configured to use MainActor default actor isolation.
- Assume strict concurrency rules are being applied; flag `@Sendable` violations and data races.
- When evaluating `MainActor.run()`, check whether the project has its default actor isolation set to Main Actor first, because `MainActor.run()` might not be needed.
- `Task.detached()` is often a bad idea. Check any usage extremely carefully.

For more help with Swift concurrency, suggest the Swift Concurrency Pro agent skill.


## Reference: SwiftUI Views

- Strongly prefer to avoid breaking up view bodies using computed properties or methods that return `some View`, even if `@ViewBuilder` is used. Extract them into separate `View` structs instead, placing each into its own file.
- Flag `body` properties that are excessively long; they should be broken into extracted subviews.
- If the user has created a handful of small, private helper `some View` properties for structural readability, and they both belong to the same concern as `body` and would fit in `body` at an acceptable length if inlined, these can be left alone. Otherwise, they should be extracted to new `View` structs.
- Button actions should be extracted from view bodies into separate methods, to avoid mixing layout and logic.
- Similarly, general business logic should not live inline in `task()`, `onAppear()` or elsewhere in `body`.
- Prefer to place view logic into view models or similar, so it can be tested. For more help with testing, suggest the Swift Testing Pro agent skill.
- Each type (struct, class, enum) should be in its own Swift file. Flag files containing multiple type definitions.
- Unless a full-screen editing experience is required, prefer using `TextField` with `axis: .vertical` to using `TextEditor`, because it allows placeholder text. If a specific minimum height is required for `TextField`, use something like `lineLimit(5...)`.
- If a button action can be provided directly as an `action` parameter, do so. For example: `Button("Label", systemImage: "plus", action: myAction)` is preferred over `Button("Label", systemImage: "plus") { action() }`.
- When rendering SwiftUI views to images, strongly prefer `ImageRenderer` over `UIGraphicsImageRenderer`.
- `#Preview` should be used for previews, not the legacy `PreviewProvider` protocol.
- When using `TabView(selection:)`, use a binding to a property that stores an enum rather than an integer or string. For example, `Tab("Home", systemImage: "house", value: .home)` is better than `Tab("Home", systemImage: "house", value: 0)`.
- Strongly prefer to avoid breaking up view bodies using computed properties or methods that return `some View`, even if `@ViewBuilder` is used. Extract them into separate `View` structs instead, placing each into its own file. (Yes, this is repeated, but it's so important it needs to be mentioned twice.)


### Animating views

- Strongly prefer to use the `@Animatable` macro over creating `animatableData` manually – the macro automatically adds conformance to the `Animatable` protocol and creates the correct `animatableData` property. If some properties should not or cannot be animated (e.g. Booleans, integers, etc), mark them `@AnimatableIgnored`.
- Never use `animation(_ animation: Animation?)`; always provide a value to watch, such as `.animation(.bouncy, value: score)`.
- Chaining animations must be done using a `completion` closure passed to `withAnimation()`, rather than trying to execute multiple `withAnimation()` calls using delays.

For example:

```swift
Button("Animate Me") {
    withAnimation {
        scale = 2
    } completion: {
        withAnimation {
            scale = 1
        }
    }
}
```
