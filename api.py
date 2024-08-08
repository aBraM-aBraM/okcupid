"""
Requirements:
* get list of available girls
* send like with message
"""

import requests

OKCUPID = "https://okcupid.com/graphql?operationName="


def get_available_partners():
    response = requests.post(f"{OKCUPID}StacksMenuQuery",
                             json={
                                 "operationName": "StacksMenuQuery",
                                 "query": "query StacksMenuQuery($includeProfileDetails: Boolean = false ) { me { __typename id stacks { __typename ...ApolloDoubleTakeStack } likesCap { __typename ...ApolloLikesCap } hasPhotos ...ApolloAdInfo } }  fragment ProfilePhotoComment on ProfileCommentPhoto { type photo { original square800 } }  fragment ProfileEssayComment on ProfileCommentEssay { type essayText essayTitle }  fragment Details on User { children identityTags relationshipStatus relationshipType drinking pets weed ethnicity smoking politics bodyType height astrologicalSign diet knownLanguages genders orientations pronounCategory customPronouns occupation { title employer status } education { level school { id name } } religion { value modifier } globalPreferences { relationshipType { values } connectionType { values } gender { values } } }  fragment DoubleTakeStackUser on StackMatch { stream targetLikesSender match { matchPercent targetLikes targetLikeViaSpotlight targetLikeViaSuperBoost firstMessage { attachments { __typename ...ProfilePhotoComment ...ProfileEssayComment } text id } user { __typename id badges { name } ...Details @include(if: $includeProfileDetails) photos { id caption width height crop { upperLeftX upperLeftY lowerRightX lowerRightY } original original558x800 square400 square100 } userLocation { publicName } essaysWithUniqueIds { id groupId title processedContent } displayname age isOnline } targetVote senderVote } profileHighlights { __typename ... on QuestionHighlight { id question answer explanation } ... on PhotoHighlight { id caption url } } hasSuperlikeRecommendation selfieVerifiedStatus }  fragment DoubleTakeFirstPartyAd on FirstPartyAd { id }  fragment DoubleTakeThirdPartyAd on ThirdPartyAd { ad }  fragment PromotedQuestions on PromotedQuestionPrompt { promotedQuestionId }  fragment ApolloDoubleTakeStack on Stack { id status expireTime votesRemaining badge data { __typename ...DoubleTakeStackUser ...DoubleTakeFirstPartyAd ...DoubleTakeThirdPartyAd ...PromotedQuestions } }  fragment ApolloLikesCap on LikesCap { likesCapTotal likesRemaining viewCount resetTime }  fragment ApolloAdInfo on User { age userLocation { publicName } binaryGenderLetter }",
                                 "variables": {
                                     "includeProfileDetails": False
                                 }
                             },
                             cookies={
                                 "override_session": "0",
                                 "siftsession": "247758351582095114",
                                 "secure_login": "1",
                                 "secure_check": "1",
                                 "session": "10580259781379019888%3A8809685390191615780"
                             },
                             headers={
                                 "x-emb-path": "/graph/ql/StackMenuQuery"
                             })
    print(response)
    print(response.json())


get_available_partners()
