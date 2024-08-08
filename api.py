import asyncio
import httpx

body = """
    {"operationName":"StacksMenuQuery","variables":{"includeProfileDetails":false},"query":"query StacksMenuQuery($includeProfileDetails: Boolean = false ) { me { __typename id stacks { __typename ...ApolloDoubleTakeStack } likesCap { __typename ...ApolloLikesCap } hasPhotos ...ApolloAdInfo } }  fragment ProfilePhotoComment on ProfileCommentPhoto { type photo { original square800 } }  fragment ProfileEssayComment on ProfileCommentEssay { type essayText essayTitle }  fragment Details on User { children identityTags relationshipStatus relationshipType drinking pets weed ethnicity smoking politics bodyType height astrologicalSign diet knownLanguages genders orientations pronounCategory customPronouns occupation { title employer status } education { level school { id name } } religion { value modifier } globalPreferences { relationshipType { values } connectionType { values } gender { values } } }  fragment DoubleTakeStackUser on StackMatch { stream targetLikesSender match { matchPercent targetLikes targetLikeViaSpotlight targetLikeViaSuperBoost firstMessage { attachments { __typename ...ProfilePhotoComment ...ProfileEssayComment } text id } user { __typename id badges { name } ...Details @include(if: $includeProfileDetails) photos { id caption width height crop { upperLeftX upperLeftY lowerRightX lowerRightY } original original558x800 square400 square100 } userLocation { publicName } essaysWithUniqueIds { id groupId title processedContent } displayname age isOnline } targetVote senderVote } profileHighlights { __typename ... on QuestionHighlight { id question answer explanation } ... on PhotoHighlight { id caption url } } hasSuperlikeRecommendation selfieVerifiedStatus }  fragment DoubleTakeFirstPartyAd on FirstPartyAd { id }  fragment DoubleTakeThirdPartyAd on ThirdPartyAd { ad }  fragment PromotedQuestions on PromotedQuestionPrompt { promotedQuestionId }  fragment ApolloDoubleTakeStack on Stack { id status expireTime votesRemaining badge data { __typename ...DoubleTakeStackUser ...DoubleTakeFirstPartyAd ...DoubleTakeThirdPartyAd ...PromotedQuestions } }  fragment ApolloLikesCap on LikesCap { likesCapTotal likesRemaining viewCount resetTime }  fragment ApolloAdInfo on User { age userLocation { publicName } binaryGenderLetter }"}
"""

async def fetch():
    client = httpx.AsyncClient()
    response = await client.request(
        method="POST",
        url="https://okcupid.com/graphql",
        params={
        "operationName":"StacksMenuQuery"
    },
        headers={
            "user-agent":"Android 91.3.0",
            "content-type":"application/json"
        },
        cookies={
        "session":"10580259781379019888%3A8809685390191615780"
    },
        content=body,
        

    )

    print(response.text)

    await client.aclose()

asyncio.run(fetch())
