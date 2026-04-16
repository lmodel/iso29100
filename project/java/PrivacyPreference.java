package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Schema class capturing a PII principal's processing choices for a particular purpose scope: preferences for anonymity or pseudonymity, restrictions on specific processing operations, and restrictions on disclosure to named or categorized parties.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrivacyPreference extends NamedEntity {

  private String principalRef;
  private String preferenceScope;
  private boolean anonymityPreference;
  private boolean pseudonymityPreference;
  private List<String> processingRestrictionPreferences;
  private List<String> disclosureRestrictionPreferences;
  private LocalDate preferenceRecordedDate;

}