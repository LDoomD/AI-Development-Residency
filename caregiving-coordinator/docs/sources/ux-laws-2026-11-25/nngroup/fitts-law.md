# Fitts's Law and Its Applications in UX
- Source: https://www.nngroup.com/articles/fitts-law/
- Author: Raluca Budiu
- Retrieved: 2026-11-25 with Firecrawl
- Page date: July 31, 2022
- Complete: yes
---
[Saved text: the cookie-consent text, the membership banner, image links (image captions kept) and the closing "Related Courses / Learn More / Related Articles" lists were left out. Article body and references are complete.]

Summary: The movement time to a target depends on the size of the target and the distance to the target.

## History

Paul Fitts was one of the first psychologists who understood that human error is attributable to poor design as opposed to just human fallacy. He studied airplane-cockpit design during World War II and argued that many losses that had been attributed to human error were, in fact, due to poor design.

In the 1950s, he became influenced by the Shannon’s famous [information theory](https://www.nngroup.com/articles/scaling-user-interfaces/). Like George Miller, who applied the concept of channel capacity to human memory and, in the process, came up with the [famous magical number 7](https://www.nngroup.com/articles/chunking/) as the bandwidth of human [short-term memory](https://www.nngroup.com/articles/short-term-memory-and-web-usability/), Fitts aimed to find the bandwidth of human movement — how many repetitive movements could be performed in a given time interval. He did several experiments involving such repetitive movements and as a result he came up with Fitts’s law, one of the most famous laws of human-computer interaction.

## Fitts’s Law

Fitts’s law gives us the relationship between the time it takes a **pointer** (such as a mouse cursor, a human finger, or a hand) to move to a particular **target** (e.g., physical or digital button, a physical object) in order to interact with it in some way (e.g., by clicking or tapping it, grasping it, etc.):

[Equation image: Movement time T is equal to a plus b multiplied by log of the ratio of two D and w]

where _D_ is the distance to the target, _w_ is the width of the target (technically, measured along the axis of movement), and _a_ and _b_ are constants that vary depending on the type of pointer (e.g., mouse, finger, etc.).

The quantity

[Equation image: ID equals log of the ratio between two D and w]

is sometimes called an index of difficulty and is measured in bits. An alternative formulation of Fitts’s law is then:

[Equation image: T equals a plus b times log 2D divided by w]

Technically, Fitts’s law equation uses the width of the target in the direction of the movement, but, for most rectangular targets that are common in user interfaces, we can replace it with the smallest of the target dimensions, whether it’s height or width (as shown by Scott MacKenzie and Bill Buxton in 1992).

If this mathematical equation seems obscure to some of you, its gist is captured by the following two statements below:

1. **The bigger the distance to the target, the longer it will take for the pointer to move to it.** In other words, closer targets are faster to acquire.
2. **The larger the target, the shorter the movement time to it.** In other words, bigger targets are better.

_Fitts’ s law says that the time to reach Target A is shorter than the time to reach any of the other targets. Although Targets A and B have the same size, the distance from cursor to A (D1) is shorter than the distance to B (D2), so movement to A will be faster. Target C is placed at the same distance (D1) from the cursor as Target A, but it’s smaller, so it will take longer to move the cursor to it than to A._

The equation includes a logarithm — meaning that the time doesn’t grow linearly with the parameters, but at a slower pace. So, if something is twice as far away, it takes longer to reach it, but not twice as long. That is because movement first accelerates and then decelerates (as described in the next section), meaning that you get to move the pointer at a higher speed during part of the travel time when the distance is longer, and then more slowly as you get closer.

This is exactly the essence of the two-component model described below.

## Two-Component Model

Well before Fitts, at the end of the 19th century, one of the pioneers of human-movement research, R. S. Woodworth, presented his two-component model of upper-limb physical movement. The model said that any goal-directed movement (e.g., performed to acquire a target as opposed to, say, tapping in the rhythm of music) can be decomposed into two components (hence the name):

1. an **initial movement**, rapid and relatively coarse, which is intended to move the pointer in the direction of the target
2. **a final movement**, which is slower and intended to secure accuracy (for example, ensure that the target is acquired correctly)

The first phase is largely driven by the distance to the target — the movement will aim to take the pointer in the direction of the target as fast as possible. **The second movement phase is, however, driven mostly by size of the target** — the pointer needs to **slow down in order to not overshoot and click beyond the target**. The smaller the target, the more time tends to be spent in this second phase.

## Applications to UX

The implications of Fitts’s law can be grouped into 2 distinct categories, corresponding to the two variables that affect the movement time: target size and distance to target.

### Optimizing Target Size

#### Bigger Is Better

The most obvious implication of Fitts’s law is: make targets big. Fitts’s law clearly says that people will be faster to click, tap, or hover on bigger targets. Not only that, but error rates go down as target sizes increases. [Guidelines for target size](https://www.nngroup.com/articles/touch-target-size/) are usually created by determining the rate of error for various target sizes and identifying the size at which the error rate levels off.

#### Icons Plus Labels

We’ve said many times that [icons need labels](https://www.nngroup.com/articles/icon-usability/). Not only does a text label reduce icon ambiguity and makes it easy to understand, but it also improves movement time to that particular target. Why? It’s simple: any target made up of both an icon and a label will be greater than just an icon and, therefore, according to Fitts’s law, will be easier to acquire. (This, of course, assumes that you do make the entire area clickable and avoid the design mistake of only making the icon itself the active target.)

_The target area for an icon will be smaller than the target area for that icon plus a text label._

#### Infinite Targets Along Screen Edges

In the two-component model, the final-movement component can be greatly reduced if the target is very big — or even infinite. With an infinite target, there is no worry that you’ll overshoot since it doesn’t matter where the pointer stops its movement (of course, provided the target area has been reached).

_With an infinite target, there is no danger of overshooting: users don’t need to slow down as they approach the target and so the movement time is low._

At this point, you may ask: Where in real-world interface design do we have infinite targets? The answer is on the **screen edges, as long as the interaction is mouse-driven**. Indeed, the screen edges act as natural walls for the cursor — as soon as the pointer reaches an edge, it cannot move beyond it, regardless of the speed with which that wall has been hit.

So technically, in order to reach a target placed on the edge of the screen, the user doesn’t have to slow down as much as if the target was in the middle of the screen because there is no danger of overshooting – the pointer will be automatically stopped once it hits the edge of the screen.

Operating-system designers have taken advantage of this consequence of Fitts law. In MacOS, application menus are shown at the very top of the screen, on the horizontal edge. This enables the user to reach that area very easily.  In Windows (at least until Windows 8) the start button was placed in the bottom left corner of the screen. In both operating systems, icons for various frequently used applications are placed along the bottom of the screen.

_In MacOS, the application menu is placed at the top edge of the screen, which acts as an infinite edge. This placement optimizes movement time to this frequently accessed area, as the options in the menu become infinite targets and users will not need to slow down in order to hit them accurately._

_In Windows, the task bar hosting a variety of commonly used apps, is shown at the bottom of the screen. This location also optimizes movement time because the application icons become infinite targets_.

Note, however, that while the edge placement offers an advantage in mouse- or trackball-driven UIs, it offers no advantage for touchscreens. In fact, a study by Daniel Avrahami showed that, for touchscreen devices, it actually takes longer to hit targets placed around the edges, possibly because for touchscreens, it is possible to overshoot and hit beyond the edge of the screen.

#### Don’t Crowd Targets

If you place targets too close to each other, there is a risk that people will accidentally overshoot and accidentally trigger the wrong target. Note that this is especially likely to happen if the targets are small.

#### Padding Is Not Enough

Sometimes designers will pad certain targets, thus increasing the effective target area. However, remember that, even though padding will help prevent some overshooting errors, if people do not realize that a target is padded, they may still cautiously slow down more than necessary as they get closer to the target, in order to make sure they will not go beyond the target area.

_A padded target is usually a small target that has a bigger invisible active area around it. If people don’t realize that a target is padded, they will still slow down as they approach it in order to make sure they hit the visible area._

### Optimizing Distance to Target

#### Menu Design

The type of menu used for displaying a list of items will play a role in movement time to any of those items. To see why, let’s look at three different menus: [a linear menu, a rectangular menu (otherwise known as a mega menu), and a pie menu.](https://www.nngroup.com/articles/expandable-menus/)

Let’s assume that, when the menu is opened, the pointer is on the menu handle or label. (This is a realistic assumption in mouse-based interfaces. Even though people will occasionally use [keyboard access keys](https://www.nngroup.com/articles/ui-copy/) to open up a menu, the more common scenario is that the menu was opened using the mouse.)

_The average distance from menu handle to a menu element depends on the type of menu: linear menus are less efficient than rectangular menus, which, in turn, are less efficient than pie menus._

In the linear menu, you can see that the distance from the menu handle to the first element in the menu is the shortest and the distance to the last element in the menu is the longest. Therefore, with such a menu, you may consider ordering items according to their frequency of use (with the most frequently accessed ones at the top).

In a rectangular menu, items are arranged along both the horizontal and vertical dimensions and, thus, the average distance to a menu option is lower than if the menu was linear.

Last, in a pie menu, all menu elements are placed on a circle around the handle and thus are equally far away from the handle. As a result, the time to reach any of these options will be the same. (In spite of this great benefit of pie menus, they remain still relatively unused in UI design and, because of that, unfamiliar to users.)

Even for the humble linear menu, if all elements are accessed relatively equally, average movement time can be improved by aligning the handle with the middle of the menu so that the farthest elements are the first and the last, and the closest one is that in the middle.

_The average movement time in a linear menu can be improved by aligning the handle with the middle of the menu._

On mobile, some contextual menus show the associated options in a bottom sheet that appears far away from the menu label. This design is suboptimal, since it forces the users to waste movement time. Ideally, the options should appear close to the label.

_Left: Gmail for iOS placed the options associated with the contextual ellipsis menu in a bottom sheet, far away from the menu handle. To select a menu option, users would have to move their finger a relatively long distance from the menu handle to the menu options. Right: In Mail for iOS, the contextual menu associated with the_ Delete _icon appeared immediately next to that icon, minimizing movement time._

#### Place Related Targets Close to Each Other

If you know that a set of controls will be clicked in a certain order, [place them close to each other](https://www.nngroup.com/articles/closeness-of-actions-and-objects-gui/) (but not too close — see guideline above) to minimize the distance between them and optimize overall task time.

For example, the _Submit_ button in a form should be placed next to the last form field. [Mobile designs that place the _Submit_ button at the very top of the page](https://www.nngroup.com/articles/4-ios-rules-break/), in the page header, not only go against the natural, top-down direction of the users’ workflow, but also result in suboptimal movement time because the user needs to move their finger from the last form field, low on the screen, to the very top of the screen.

_Left: Sephora for iPhone places the_ Save _button in the top right corner of the screen. The user’s finger needs to travel a relatively long way from the last field of the form to the_ Save _button. Right: In contrast, Taxa 4x35, a Danish taxi app, places the main call to action at the very bottom of the form, close to the last form field._

## Conclusion

Fitts’s law says that the time to move to a target depends on how big it is and on how far away it is.  As you are creating new UI designs, think about optimizing both these variables by creating well-spaced, big targets and positioning them so that they are close to the user’s most probable prior location.

## References

Avrahami, D. 2015.The Effect of Edge Targets on Touch Performance _. CHI’15._

Elliott, D., Helsen, W. F., & Chua, R. (2001). A century later: Woodworth's (1899) two-component model of goal-directed aiming. _Psychological Bulletin, 127_(3), 342–357. [https://doi.org/10.1037/0033-2909.127.3.342](https://psycnet.apa.org/doi/10.1037/0033-2909.127.3.342)

Fitts, Paul M. (June 1954). "The information capacity of the human motor system in controlling the amplitude of movement". _Journal of Experimental Psychology_. **47** (6): 381–391. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)): [10.1037/h0055392](https://doi.org/10.1037%2Fh0055392)

I. Scott MacKenzie and William Buxton. 1992. Extending Fitts' law to two-dimensional tasks. In _CHI '92_. New York, NY, USA, 219–226. https://doi.org/10.1145/142750.142794
