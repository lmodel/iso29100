package example;

/* metamodel_version: 1.12.0 */
/* version: 2024 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One organization's use of the privacy framework: the systems it covers, and every record the organization keeps about them, each kind in a list of its own.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PfFramework  {

  private List<String> pfJurisdictions;
  private String pfOrganization;
  private List<String> pfIctSystems;
  private List<PfActor> pfActors;
  private List<PfPiiItem> pfPiiItems;
  private List<PfPiiFlow> pfFlows;
  private List<PfProcessingActivity> pfProcessingActivities;
  private List<PfSafeguardingRequirement> pfSafeguardingRequirements;
  private List<PfPolicy> pfPolicies;
  private List<PfControl> pfControls;
  private List<PfPrincipleImplementation> pfPrincipleImplementations;
  private List<PfRisk> pfRisks;
  private List<PfImpactAssessment> pfImpactAssessments;
  private List<PfBreach> pfBreaches;
  private List<PfConsent> pfConsents;
  private List<PfPreference> pfPreferences;
  private URI pfId;
  private String title;
  private String description;


}