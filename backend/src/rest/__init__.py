from .UserResource import users_list_ns
from .InscritResource import inscrits_list_ns
from .MembreFamilleResource import membre_familles_list_ns
from .CiqualResource import ciquals_list_ns
from .PATResource import pats_list_ns
from .PartenaireSanteClimatResource import partenaire_sante_climats_list_ns
from .PreferencesResource import preferences_list_ns
from .PlatResource import plats_list_ns
from .MenuResource import menus_list_ns
from .EntreeResource import entrees_list_ns
from .DessertResource import desserts_list_ns
from .EncasResource import encas_list_ns
from .VinaigretteResource import vinaigrettes_list_ns
from .ProgrammeHebdomadaireResource import programme_hebdomadaire_list_ns
from .FrontendResource import frontend_inscription_ns
from .FrontendResource import frontend_infos_ns
from .FrontendResource import frontend_preferences_ns
from .FrontendResource import frontend_famille_ns
from .FrontendResource import frontend_menus_ns
from .AccountResource import account_register_ns
from .AccountResource import account_login_ns
from .AccountResource import account_confirm_ns
from .AccountResource import account_resend_ns
from .AccountResource import account_forgot_password_ns
from .AccountResource import account_reset_password_ns


def add_api_namespace(api):
    # Registering the namespaces
    api.add_namespace(account_register_ns)
    api.add_namespace(account_login_ns)
    api.add_namespace(account_confirm_ns)
    api.add_namespace(account_resend_ns)
    api.add_namespace(account_forgot_password_ns)
    api.add_namespace(account_reset_password_ns)
    api.add_namespace(frontend_inscription_ns)
    api.add_namespace(frontend_infos_ns)
    api.add_namespace(frontend_preferences_ns)
    api.add_namespace(frontend_famille_ns)
    api.add_namespace(frontend_menus_ns)
    api.add_namespace(users_list_ns)
    api.add_namespace(inscrits_list_ns)
    api.add_namespace(membre_familles_list_ns)
    api.add_namespace(pats_list_ns)
    api.add_namespace(preferences_list_ns)
    api.add_namespace(partenaire_sante_climats_list_ns)
    api.add_namespace(ciquals_list_ns)
    api.add_namespace(plats_list_ns)
    api.add_namespace(menus_list_ns)
    api.add_namespace(entrees_list_ns)
    api.add_namespace(desserts_list_ns)
    api.add_namespace(encas_list_ns)
    api.add_namespace(vinaigrettes_list_ns)


    account_register_ns.add_resource(AccountResource.UserRegister, "")
    account_confirm_ns.add_resource(AccountResource.ConfirmEmail, "/<string:token>")
    account_login_ns.add_resource(AccountResource.UserLogin, "")
    account_resend_ns.add_resource(AccountResource.ResendEmail, "")
    account_forgot_password_ns.add_resource(AccountResource.ForgotPassword, "")
    account_reset_password_ns.add_resource(
        AccountResource.ResetPassword, "/<string:token>"
    )
    frontend_inscription_ns.add_resource(
        FrontendResource.FormulaireInscriptionResource, ""
    )
    frontend_infos_ns.add_resource(FrontendResource.InscritInfosResource, "")
    frontend_preferences_ns.add_resource(
        FrontendResource.InscritPreferencesResource, ""
    )
    frontend_famille_ns.add_resource(FrontendResource.InscritFamilleResource, "")
    frontend_menus_ns.add_resource(FrontendResource.InscritMenusResource, "")
    users_list_ns.add_resource(UserResource.UserResourceList, "")
    users_list_ns.add_resource(UserResource.UserResourceListCount, "/count")
    users_list_ns.add_resource(UserResource.UserResource, "/<int:id>")
    inscrits_list_ns.add_resource(InscritResource.InscritResourceList, "")
    inscrits_list_ns.add_resource(InscritResource.InscritResourceListCount, "/count")
    inscrits_list_ns.add_resource(InscritResource.InscritResource, "/<int:id>")
    membre_familles_list_ns.add_resource(
        MembreFamilleResource.MembreFamilleResourceList, ""
    )
    membre_familles_list_ns.add_resource(
        MembreFamilleResource.MembreFamilleResourceListCount, "/count"
    )
    membre_familles_list_ns.add_resource(
        MembreFamilleResource.MembreFamilleResource, "/<int:id>"
    )
    ciquals_list_ns.add_resource(CiqualResource.CiqualResourceList, "")
    ciquals_list_ns.add_resource(CiqualResource.CiqualResourceListCount, "/count")
    ciquals_list_ns.add_resource(CiqualResource.CiqualResource, "/<int:id>")
    pats_list_ns.add_resource(PATResource.PATResourceList, "")
    pats_list_ns.add_resource(PATResource.PATResourceListCount, "/count")
    pats_list_ns.add_resource(PATResource.PATResource, "/<int:id>")
    partenaire_sante_climats_list_ns.add_resource(
        PartenaireSanteClimatResource.PartenaireSanteClimatResourceList, ""
    )
    partenaire_sante_climats_list_ns.add_resource(
        PartenaireSanteClimatResource.PartenaireSanteClimatResourceListCount, "/count"
    )
    partenaire_sante_climats_list_ns.add_resource(
        PartenaireSanteClimatResource.PartenaireSanteClimatResource, "/<int:id>"
    )
    preferences_list_ns.add_resource(PreferencesResource.PreferencesResourceList, "")
    preferences_list_ns.add_resource(
        PreferencesResource.PreferencesResourceListCount, "/count"
    )
    preferences_list_ns.add_resource(
        PreferencesResource.PreferencesResource, "/<int:id>"
    )
    plats_list_ns.add_resource(PlatResource.PlatResourceList, "")
    plats_list_ns.add_resource(
        PlatResource.PlatResourceListCount, "/count"
    )
    plats_list_ns.add_resource(
        PlatResource.PlatResource, "/<int:id>"
    )
    menus_list_ns.add_resource(MenuResource.MenuResourceList, "")
    menus_list_ns.add_resource(
        MenuResource.MenuResourceListCount, "/count"
    )
    menus_list_ns.add_resource(
        MenuResource.MenuResource, "/<int:id>"
    )
    entrees_list_ns.add_resource(EntreeResource.EntreeResourceList, "")
    entrees_list_ns.add_resource(
        EntreeResource.EntreeResourceListCount, "/count"
    )
    entrees_list_ns.add_resource(
        EntreeResource.EntreeResource, "/<int:id>"
    )
    desserts_list_ns.add_resource(DessertResource.DessertResourceList, "")
    desserts_list_ns.add_resource(
        DessertResource.DessertResourceListCount, "/count"
    )
    desserts_list_ns.add_resource(
        DessertResource.DessertResource, "/<int:id>"
    )
    encas_list_ns.add_resource(EncasResource.EncasResourceList, "")
    encas_list_ns.add_resource(
        EncasResource.EncasResourceListCount, "/count"
    )
    encas_list_ns.add_resource(
        EncasResource.EncasResource, "/<int:id>"
    )
    vinaigrettes_list_ns.add_resource(VinaigretteResource.VinaigretteResourceList, "")
    vinaigrettes_list_ns.add_resource(
        VinaigretteResource.VinaigretteResourceListCount, "/count"
    )
    vinaigrettes_list_ns.add_resource(
        VinaigretteResource.VinaigretteResource, "/<int:id>"
    )
    programme_hebdomadaire_list_ns.add_resource(ProgrammeHebdomadaireResource.ProgrammeHebdomadaireResourceList, "")
    programme_hebdomadaire_list_ns.add_resource(
        ProgrammeHebdomadaireResource.ProgrammeHebdomadaireResourceListCount, "/count"
    )
    programme_hebdomadaire_list_ns.add_resource(
        ProgrammeHebdomadaireResource.ProgrammeHebdomadaireResource, "/<int:id>"
    )
    

    return api
