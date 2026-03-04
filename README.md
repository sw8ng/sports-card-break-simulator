# Sports Card Break Simulator

## Purpose

The goal of this project is to build a realistic simulation of sports card breaking and eventually develop it into a web application. It is designed to model the system end-to-end, including pack and box odds, team assignment for participants, card ownership tracking, and analysis of outcomes such as pull distributions and profitability. The project will be built in phases, starting with a working simulation engine and expanding into a deployable web application with a user interface.

This project also serves as a way for me to gain deeper hands-on experience with backend application design, APIs, and databases, by applying them in a practical project. 

---

## What is a card break?

In the sports card hobby, a “break” refers to a group purchase of sealed trading card products—most commonly full cases—where participants buy the rights to specific teams, players, or divisions. As packs are opened live, any cards pulled that match a participant’s assigned slot belong to them. This allows collectors to participate in opening expensive products without having to purchase an entire case themselves. The individuals or businesses who host the breaks are referred to as breakers. They typically purchase sealed cases and sell the individual teams or slots at prices that collectively exceed the cost of the case, allowing them to make a profit if all spots fill.

Over the past decade, the sports trading card industry has grown significantly, with individual cards sometimes selling for thousands, hundreds of thousands, or even millions of dollars. Many collectors participate in breaks for the excitement and anticipation of pulling a valuable or personally meaningful card. However, the outcome of a break is highly uncertain—some participants may pull cards worth far more than what they paid, while others may end up getting skunked, meaning they receive little or nothing of value from the break. This simulator models the mechanics behind these breaks, including card rarity, distribution of pulls, the likelihood of getting skunked, and the potential financial outcomes such as profit or loss.

---

## Motivation

After taking a semester off from university in Fall 2025 for health reasons, I found myself with more time to slow down, recover, and explore new hobbies. Collecting cards of athletes I enjoy watching quickly became something I found really fun, and I soon built a personal collection full of childhood heroes and potential world beaters. During that time I also participated in many online card breaks. Waiting to see what cards come out creates a real dopamine rush — sometimes I hit a card that’s perfect for my personal collection, and sometimes I walk away with very little or nothing at all.

Through those experiences, I started thinking more about the odds and financial side of card breaking. The cost of participating in breaks often outweighs the value of the cards pulled, which makes the experience similar to other forms of chance-based entertainment often seen in casinos. This project aims allow users to experience the excitement of opening packs and participating in breaks without spending real money. It also provides a way to explore the probabilities and outcomes behind the hobby in a more analytical way.

---

## Product Types

Card breaks can involve different types of sealed products. Each level of product affects how cards are distributed and what odds participants might expect.

**Full Cases** <br/>
A sealed case containing multiple boxes (often around 8–12 depending on the product). Many products include “case hits,” which are rare cards expected to appear about once per case on average. Because of this, breaks that open a full case have the best chance of producing these rare pulls.

**Full Boxes** <br/>
A sealed hobby box opened as part of a break. Boxes typically contain a fixed number of packs and often guarantee certain types of cards, such as autographs or relic cards. However, boxes do not always guarantee case-level hits.

**Loose Boxes** <br/>
Entire hobby boxes opened outside of their original case. Since some rare cards are distributed at the case level, opening loose boxes may result in none of the case hits appearing, even if multiple boxes are opened.

**Loose Packs** <br/>
Individual packs opened outside of a box or case. Because they are removed from the larger product structure, pack-level pulls may not reflect the odds expected when opening a full box or case.

---

## Break Formats

This simulator aims to model several common formats used in real sports card breaks:

**Random Teams** <br/>
Participants purchase a spot in the break and teams are assigned randomly before packs are opened. This format is common when the price of certain teams would otherwise be significantly higher than others.

**Pick Your Team (PYT)** <br/>
Participants choose and purchase a specific team before the break begins. Any cards pulled from packs that correspond to that team are assigned to the participant who selected it.

**Pick Your Player (PYP)** <br/>
In some breaks, participants purchase the rights to specific players instead of teams. Any cards pulled featuring that player belong to the participant who selected them.

---

## Card Types and Rarity

Sports card products contain different types of cards that vary in rarity and desirability. 

**Card Categories**

**- Base Cards** <br/>
Base cards make up the main checklist of a product and appear most frequently in packs.

**- Insert Cards** <br/>
Insert cards are special subsets that appear less frequently than base cards and usually feature unique themes or designs.

**- Autographs** <br/>
Autograph cards contain a player's signature and are typically considered premium pulls.

**- Relics** <br/>
Relic cards contain pieces of player-worn or game-used memorabilia such as jersey patches. Some cards combine both relics and autographs.

**Designations**

**- Rookie Cards** <br/>
Rookie cards feature players in their first official card release. Rookie cards may appear in the base set, inserts, autographs, relics, or other special cards.

**- Case Hits** <br/>
Case hits are extremely rare cards that typically appear once per sealed case rather than per box. These cards are often special inserts or unique designs intended to be some of the most desirable pulls in a product.

**Rarity Modifiers**

**- Parallels** <br/>
Many cards appear in parallel versions that use different colors, finishes, or designs compared to the standard version of the card. Parallels are typically rarer than the base version and may appear at different pull rates depending on the product. Both base cards and inserts can have parallel variations.

Some parallels are serial numbered, meaning they have a limited print run that indicates how many copies exist (for example /199, /50, /10, or /1). In this simulator, serial numbering will be simplified to represent the print run size (for example /400) rather than tracking the exact individual number (such as 053/400).

**- Short Prints (SP)** <br/>
Short print cards are special parallels produced in smaller quantities than standard cards and are mostly not serial numbered.

Many cards combine multiple characteristics—for example, a rookie autograph that is also serial numbered, or an insert that appears as a limited parallel.
