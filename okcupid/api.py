import json
import httpx
from httpx import Response

from okcupid import consts
from okcupid.models import User

STACK_MENU_QUERY = "StacksMenuQuery"
OPERATION_TO_BODY = {
    STACK_MENU_QUERY: """{"operationName":"StacksMenuQuery","variables":{"includeProfileDetails":false},"query":"query StacksMenuQuery($includeProfileDetails: Boolean = false ) { me { __typename id stacks { __typename ...ApolloDoubleTakeStack } likesCap { __typename ...ApolloLikesCap } hasPhotos ...ApolloAdInfo } }  fragment ProfilePhotoComment on ProfileCommentPhoto { type photo { original square800 } }  fragment ProfileEssayComment on ProfileCommentEssay { type essayText essayTitle }  fragment Details on User { children identityTags relationshipStatus relationshipType drinking pets weed ethnicity smoking politics bodyType height astrologicalSign diet knownLanguages genders orientations pronounCategory customPronouns occupation { title employer status } education { level school { id name } } religion { value modifier } globalPreferences { relationshipType { values } connectionType { values } gender { values } } }  fragment DoubleTakeStackUser on StackMatch { stream targetLikesSender match { matchPercent targetLikes targetLikeViaSpotlight targetLikeViaSuperBoost firstMessage { attachments { __typename ...ProfilePhotoComment ...ProfileEssayComment } text id } user { __typename id badges { name } ...Details @include(if: $includeProfileDetails) photos { id caption width height crop { upperLeftX upperLeftY lowerRightX lowerRightY } original original558x800 square400 square100 } userLocation { publicName } essaysWithUniqueIds { id groupId title processedContent } displayname age isOnline } targetVote senderVote } profileHighlights { __typename ... on QuestionHighlight { id question answer explanation } ... on PhotoHighlight { id caption url } } hasSuperlikeRecommendation selfieVerifiedStatus }  fragment DoubleTakeFirstPartyAd on FirstPartyAd { id }  fragment DoubleTakeThirdPartyAd on ThirdPartyAd { ad }  fragment PromotedQuestions on PromotedQuestionPrompt { promotedQuestionId }  fragment ApolloDoubleTakeStack on Stack { id status expireTime votesRemaining badge data { __typename ...DoubleTakeStackUser ...DoubleTakeFirstPartyAd ...DoubleTakeThirdPartyAd ...PromotedQuestions } }  fragment ApolloLikesCap on LikesCap { likesCapTotal likesRemaining viewCount resetTime }  fragment ApolloAdInfo on User { age userLocation { publicName } binaryGenderLetter }"}"""
}


class OkCupidClient:
    def __init__(self):
        self._client = httpx.Client()
        self.stack_matches: list[User] = []
        self.likes_remaining: int = -1
        self._stacks: list[dict] = []
        self._stack_menu_query()

    def _stack_menu_query(self):
        # raw_data = self.post_operation("StacksMenuQuery",
        #                       """{"operationName":"StacksMenuQuery","variables":{"includeProfileDetails":false},"query":"query StacksMenuQuery($includeProfileDetails: Boolean = false ) { me { __typename id stacks { __typename ...ApolloDoubleTakeStack } likesCap { __typename ...ApolloLikesCap } hasPhotos ...ApolloAdInfo } }  fragment ProfilePhotoComment on ProfileCommentPhoto { type photo { original square800 } }  fragment ProfileEssayComment on ProfileCommentEssay { type essayText essayTitle }  fragment Details on User { children identityTags relationshipStatus relationshipType drinking pets weed ethnicity smoking politics bodyType height astrologicalSign diet knownLanguages genders orientations pronounCategory customPronouns occupation { title employer status } education { level school { id name } } religion { value modifier } globalPreferences { relationshipType { values } connectionType { values } gender { values } } }  fragment DoubleTakeStackUser on StackMatch { stream targetLikesSender match { matchPercent targetLikes targetLikeViaSpotlight targetLikeViaSuperBoost firstMessage { attachments { __typename ...ProfilePhotoComment ...ProfileEssayComment } text id } user { __typename id badges { name } ...Details @include(if: $includeProfileDetails) photos { id caption width height crop { upperLeftX upperLeftY lowerRightX lowerRightY } original original558x800 square400 square100 } userLocation { publicName } essaysWithUniqueIds { id groupId title processedContent } displayname age isOnline } targetVote senderVote } profileHighlights { __typename ... on QuestionHighlight { id question answer explanation } ... on PhotoHighlight { id caption url } } hasSuperlikeRecommendation selfieVerifiedStatus }  fragment DoubleTakeFirstPartyAd on FirstPartyAd { id }  fragment DoubleTakeThirdPartyAd on ThirdPartyAd { ad }  fragment PromotedQuestions on PromotedQuestionPrompt { promotedQuestionId }  fragment ApolloDoubleTakeStack on Stack { id status expireTime votesRemaining badge data { __typename ...DoubleTakeStackUser ...DoubleTakeFirstPartyAd ...DoubleTakeThirdPartyAd ...PromotedQuestions } }  fragment ApolloLikesCap on LikesCap { likesCapTotal likesRemaining viewCount resetTime }  fragment ApolloAdInfo on User { age userLocation { publicName } binaryGenderLetter }"}""").text
        with open(consts.RESOURCES_DIR / "stack_menu_query.json", encoding="utf8") as rr:
            raw_data = rr.read()
        self.parse_stack_menu_query(raw_data)

    def parse_stack_menu_query(self, raw_data: str):
        data = json.loads(raw_data)["data"]["me"]
        self.likes_remaining = data["likesCap"]["likesRemaining"]
        stacks = data["stacks"]
        for stack in stacks:
            stack["data"] = [stack_match for stack_match in stack["data"]
                             if stack_match["__typename"] == "StackMatch"]

        self._stacks = sorted(stacks, key=lambda d: consts.STACK_ORDER.index(d["id"]))

        self.stack_matches = []
        for stack in self._stacks:
            for user in stack["data"]:
                user_data = user["match"]["user"]
                self.stack_matches.append(User(
                    name=user_data["displayname"],
                    age=user_data["age"],
                    photos=[photo_data["original"] for photo_data in user_data["photos"]],
                    targetLikesSender=user["targetLikesSender"],
                    user_id=user_data["id"],
                    user_content={content["title"]: content["processedContent"] for content in
                                  user_data["essaysWithUniqueIds"]},
                ))

    def send_msg(self):
        body = """
    {"operationName":"SendMessage","variables":{"input":{"text":"bongos","targetId":"12740067616428539099","gif":null,"profileComment":{"photo":{"id":"8489617191718734770","text":"bongos"}}}},"query":"mutation SendMessage($input: ConversationMessageSendInput!) { conversationMessageSend(input: $input) { success nway messageId threadId adTrigger ratingTrigger } }"}
"""
        response = self.post_operation("SendMessage", body)
        return response

    def post_operation(self, operation: str, body: str) -> Response:
        response = self._client.request(
            method="POST",
            url="https://okcupid.com/graphql",
            params={
                "operationName": operation
            },
            headers={
                "user-agent": "Android 91.3.0",
                "content-type": "application/json"
            },
            cookies={
                "session": "10580259781379019888%3A8809685390191615780"
            },
            content=body,
        )
        return response
